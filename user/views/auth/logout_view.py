from django.contrib.auth import logout
from django.http import JsonResponse
from django.views import View


class LogoutView(View):
    def post(self, request):
        logout(request)  # Clear session
        return JsonResponse({"message": "Logged out successfully"}, status=200)
