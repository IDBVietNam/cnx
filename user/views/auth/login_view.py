from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views import View

class LoginView(View):
    def post(self, request):
        c_username = request.POST.get("c_username")
        c_password = request.POST.get("c_password")

        user = authenticate(request, c_username=c_username, password=c_password)
        if user:
            login(request, user)  # Create session
            return JsonResponse({"message": "Login successful"}, status=200)
        return JsonResponse({"error": "Invalid credentials"}, status=400)
