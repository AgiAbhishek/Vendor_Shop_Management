from django.urls import path
from .views import ShopListCreate, ShopRetrieveUpdateDestroy, NearbyShops, shop_list, edit_shop, delete_shop

urlpatterns = [
    path('', shop_list, name='shop-list'),  # Render the shop list template
    path('api/', ShopListCreate.as_view(), name='shop-list-create'),  # API endpoint for listing and creating shops
    path('api/<int:pk>/', ShopRetrieveUpdateDestroy.as_view(), name='shop-retrieve-update-destroy'),  # API endpoint for retrieving, updating, and deleting shops
    path('api/nearby/', NearbyShops.as_view(), name='nearby-shops'),  # API endpoint for nearby shops
    path('edit/<int:shop_id>/', edit_shop, name='edit-shop'),  # Edit shop view
    path('delete/<int:shop_id>/', delete_shop, name='delete-shop'),  # Delete shop view
]