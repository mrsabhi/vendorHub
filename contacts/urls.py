from django.urls import path

from contacts.views import ContactView

urlpatterns = [
    path("contact", ContactView.as_view())
]
