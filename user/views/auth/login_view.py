from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/home/index")  # Redirect on success
        else:
            return render(request, "home/login.html", {"error": "Invalid credentials"})

    return render(request, "user/login.html")
