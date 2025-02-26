from django.contrib.auth import logout
from django.http import HttpRequest
from django.shortcuts import redirect


def user_logout(request: HttpRequest):
    logout(request)
    return redirect("login")  # Ensure 'login' is the name of your login URL pattern
