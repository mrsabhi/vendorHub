from django.urls import path

from vendor_accounts.views import VendorAccountsView

urlpatterns = [
    path("vendor/registrations", VendorAccountsView.as_view())
]
