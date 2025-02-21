from django.urls import path

from .views.auth.login_view import LoginView
from .views.auth.logout_view import LogoutView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
