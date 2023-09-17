from rest_framework import serializers

from vendor_accounts.models import VendorAccounts


class VendorAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorAccounts
        fields = [
            "vendor_name", "vendor_email", "vendor_phone_number", "shop_name",
            "state", "address", "pin_code", "is_vendor",
            "created_at", "updated_at",
        ]