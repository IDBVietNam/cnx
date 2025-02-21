from django.urls import path

from user.views.auth import LogoutView, user_login

urlpatterns = [
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login/", user_login, name="login"),
]
