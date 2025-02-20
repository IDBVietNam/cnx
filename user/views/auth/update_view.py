import json

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import View

User = get_user_model()


class UpdateProfileView(LoginRequiredMixin, View):
    def put(self, request):
        try:
            data = json.loads(request.body)
            user = request.user

            # Extract fields to update
            c_firstName = data.get("c_firstName")
            c_lastName = data.get("c_lastName")
            c_email = data.get("c_email")

            # Validate input
            if not any([c_firstName, c_lastName, c_email]):
                return JsonResponse(
                    {"error": "At least one field is required"}, status=400
                )

            if (
                c_email
                and User.objects.filter(c_email=c_email).exclude(id=user.id).exists()
            ):
                return JsonResponse({"error": "Email is already in use"}, status=400)

            # Update the user profile
            if c_firstName:
                user.c_firstName = c_firstName
            if c_lastName:
                user.c_lastName = c_lastName
            if c_email:
                user.c_email = c_email

            user.save()

            return JsonResponse({"message": "Profile updated successfully"}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
