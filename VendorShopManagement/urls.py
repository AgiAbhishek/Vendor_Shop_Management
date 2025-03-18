from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.views.generic import RedirectView  # Add this import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shops/', include('shops.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login endpoint
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Token refresh endpoint
    path('', RedirectView.as_view(url='shops/')),  # Redirect root URL to shops/
]