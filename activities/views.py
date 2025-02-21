from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from activities.models import Activities


def activities_form(request: HttpRequest) -> HttpResponse:
    activities = Activities.objects.all()
    return render(
        request,
        "home/activities/activities.html",
        {"activities": activities},
    )
