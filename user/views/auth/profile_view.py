from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import View


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        profile_data = {
            "c_username": user.c_username,
            "c_email": user.c_email,
            "c_firstName": user.c_firstName,
            "c_lastName": user.c_lastName,
            "dateCreated": user.dateCreated,
            "dateModified": user.dateModified,
        }
        return JsonResponse(profile_data, status=200)
