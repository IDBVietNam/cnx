from django.urls import path

from .views.auth.login_view import LoginView
from .views.auth.logout_view import LogoutView
from .views.auth.profile_view import ProfileView
from .views.auth.update_view import UpdateProfileView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("update-profile/", UpdateProfileView.as_view(), name="update-profile"),
]
