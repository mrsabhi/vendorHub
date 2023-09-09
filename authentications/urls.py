from django.urls import path

from authentications.views import RegistrationView, LoginView, LogoutView

urlpatterns = [
    path("registration", RegistrationView.as_view()),
    path("login", LoginView.as_view()),
    path("logout", LogoutView.as_view()),
]
