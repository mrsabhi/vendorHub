from django.db import models

from authentications.models import User


# Create your models here.

class VendorAccounts(models.Model):
    vendor_name = models.CharField(max_length=255)
    vendor_email = models.EmailField(unique=True)
    vendor_phone_number = models.IntegerField()
    shop_name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    pin_code = models.IntegerField()
    is_vendor = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.shop_name}~{self.vendor_name}"
