from django.urls import path

from products.views import ProductView, ProductIdView

urlpatterns = [
    path("product", ProductView.as_view()),
    path("product/<int:pk>", ProductIdView.as_view()),
]
