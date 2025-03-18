from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import Vendor, Shop

# Customize the UserAdmin for the Vendor model
class VendorAdmin(UserAdmin):
    list_display = ('username', 'email', 'name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('name', 'email')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'name', 'email', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
    search_fields = ('username', 'name', 'email')
    ordering = ('username',)

# Customize the Shop admin interface
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'business_type', 'latitude', 'longitude')
    list_filter = ('business_type', 'owner')
    search_fields = ('name', 'owner__username', 'business_type')
    raw_id_fields = ('owner',)  # Improves performance for large user databases

# Register the Vendor model with the custom admin class
admin.site.register(Vendor, VendorAdmin)

# Register the Shop model with the custom admin class
admin.site.register(Shop, ShopAdmin)

# Unregister the default Group model and re-register it (optional)
admin.site.unregister(Group)
admin.site.register(Group)

# Customize the admin interface to group models
admin.site.site_header = "Vendor Shop Management"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to Vendor Shop Management"

# Group models in the admin interface
admin.site.unregister(Group)
admin.site.register(Group)

# Create a separate section for Shops
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'business_type', 'latitude', 'longitude')
    list_filter = ('business_type', 'owner')
    search_fields = ('name', 'owner__username', 'business_type')
    raw_id_fields = ('owner',)  # Improves performance for large user databases

# Register the Shop model in a separate section
class ShopsAdminSite(admin.AdminSite):
    site_header = "Shops Management"
    site_title = "Shops Admin Portal"
    index_title = "Welcome to Shops Management"

shops_admin_site = ShopsAdminSite(name='shops_admin')
shops_admin_site.register(Shop, ShopAdmin)