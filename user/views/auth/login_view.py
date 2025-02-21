from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views import View


class LoginView(View):
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return JsonResponse({"message": "Login successful"}, status=200)
        return JsonResponse({"error": "Invalid credentials"}, status=400)
