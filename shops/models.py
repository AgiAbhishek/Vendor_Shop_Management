from django.db import models
from django.contrib.auth.models import AbstractUser, Group

# Custom user model
class Vendor(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    # Add custom related_name to avoid clashes
    groups = models.ManyToManyField(
        Group,
        related_name='vendor_groups',  # Custom related_name
        blank=True,
        verbose_name='groups',
        help_text='The groups this vendor belongs to.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='vendor_permissions',  # Custom related_name
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this vendor.',
    )

    def __str__(self):
        return self.username

# Shop model
class Shop(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(Vendor, on_delete=models.CASCADE)  # Link to the Vendor model
    business_type = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name