from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest
from django.shortcuts import redirect, render


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = None
        if username and password:
            user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("home:index")
        else:
            return render(request, "user/login.html", {"error": "Invalid credentials"})

    return render(request, "user/login.html")


def user_logout(request: HttpRequest):
    logout(request)
    return redirect("user:login")
