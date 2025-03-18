from rest_framework import generics, permissions, filters
from .models import Shop
from .serializers import ShopSerializer
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from geopy.distance import geodesic
from django.core.paginator import Paginator
from django.db.models import Q

# Custom permission to ensure only the owner can edit or delete a shop
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

# API view for listing and creating shops
class ShopListCreate(generics.ListCreateAPIView):
    serializer_class = ShopSerializer
    filter_backends = [filters.SearchFilter]  # Add search functionality
    search_fields = ['name', 'business_type']  # Fields to search

    def get_permissions(self):
        """
        Allow public access for listing shops (GET requests).
        Require authentication for creating shops (POST requests).
        """
        if self.request.method == 'GET':
            return [permissions.AllowAny()]  # Public access for listing shops
        return [permissions.IsAuthenticated()]  # Authentication required for creating shops

    def get_queryset(self):
        """
        Return all shops for public access.
        Return only shops owned by the requesting vendor for authenticated users.
        """
        if self.request.user.is_authenticated:
            return Shop.objects.filter(owner=self.request.user)
        return Shop.objects.all()  # Public access to all shops

    def perform_create(self, serializer):
        """
        Automatically set the owner to the requesting user when creating a shop.
        """
        serializer.save(owner=self.request.user)

# API view for retrieving, updating, and deleting a shop
class ShopRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]  # Only the owner can update or delete

# API view for searching nearby shops
class NearbyShops(generics.ListAPIView):
    serializer_class = ShopSerializer

    def get_queryset(self):
        user_lat = float(self.request.query_params.get('lat'))
        user_lon = float(self.request.query_params.get('lon'))
        radius = float(self.request.query_params.get('radius', 10))  # Default radius is 10 km

        shops = Shop.objects.all()
        nearby_shops = []
        for shop in shops:
            shop_coords = (shop.latitude, shop.longitude)
            user_coords = (user_lat, user_lon)
            distance = geodesic(shop_coords, user_coords).km
            if distance <= radius:
                nearby_shops.append(shop)
        return nearby_shops

# Django view for rendering the shop list template
def shop_list(request):
    """
    Render the shop list template with pagination and search functionality.
    """
    shops = Shop.objects.all()

    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        shops = shops.filter(
            Q(name__icontains=search_query) | Q(business_type__icontains=search_query)
        )
    
    # Pagination
    paginator = Paginator(shops, 10)  # Show 10 shops per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'shops/shop_list.html', {'page_obj': page_obj})

# Django view for editing a shop
from django.contrib import messages

def edit_shop(request, shop_id):
    """
    Allow the shop owner to edit their shop.
    """
    shop = get_object_or_404(Shop, id=shop_id)
    
    # Check if the requesting user is the owner of the shop
    if request.user != shop.owner:
        return JsonResponse({'error': 'You do not have permission to edit this shop.'}, status=403)

    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        business_type = request.POST.get('business_type')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        # Validate form data
        if not name or not business_type or not latitude or not longitude:
            messages.error(request, 'All fields are required.')
        else:
            try:
                # Update the shop details
                shop.name = name
                shop.business_type = business_type
                shop.latitude = float(latitude)
                shop.longitude = float(longitude)
                shop.save()
                messages.success(request, 'Shop updated successfully.')
                return redirect('shop-list')
            except ValueError:
                messages.error(request, 'Invalid latitude or longitude.')

    # Render the edit shop template with the shop data
    return render(request, 'shops/edit_shop.html', {'shop': shop})

# Django view for deleting a shop
from django.contrib import messages

def delete_shop(request, shop_id):
    """
    Allow the shop owner to delete their shop.
    """
    shop = get_object_or_404(Shop, id=shop_id)
    
    # Check if the requesting user is the owner of the shop
    if request.user != shop.owner:
        return JsonResponse({'error': 'You do not have permission to delete this shop.'}, status=403)

    if request.method == 'POST':
        shop.delete()
        messages.success(request, 'Shop deleted successfully.')
        return redirect('shop-list')
    
    return render(request, 'shops/delete_shop.html', {'shop': shop})