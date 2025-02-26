from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest
from django.shortcuts import redirect, render


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/home")  # Redirect on success
        else:
            return render(request, "user/login.html", {"error": "Invalid credentials"})

    return render(request, "user/login.html")


def user_logout(request: HttpRequest):
    logout(request)
    return redirect("login")  # Ensure 'login' is the name of your login URL pattern
