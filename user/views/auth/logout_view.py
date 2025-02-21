from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View


class LogoutView(View):
    def get(self, request):
        print("logout ne`!")
        logout(request)
        return redirect("login")  # Ensure 'login' is the name of your login URL pattern
