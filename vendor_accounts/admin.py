from django.contrib import admin

from vendor_accounts.models import VendorAccounts


# Register your models here.
@admin.register(VendorAccounts)
class VendorAccountsAdmin(admin.ModelAdmin):
    list_display = [
        "vendor_name", "vendor_email", "vendor_phone_number", "shop_name",
        "state", "address", "is_vendor", "gstin", "pin_code",
        "created_at", "updated_at",
    ]
    search_fields = ["email", "vendor_name"]
