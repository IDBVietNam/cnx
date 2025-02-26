from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from activities.models import Activities


def activities_form(request: HttpRequest) -> HttpResponse:
    if not request.headers.get("HX-Request"):
        return redirect("base:404")
    activities = Activities.objects.all()
    return render(
        request,
        "home/activities/activities.html",
        {"activities": activities},
    )


def test_telesales(request: HttpRequest) -> HttpResponse:
    if not request.headers.get("HX-Request"):
        return redirect("base:404")
    return render(request, "home/activities/test_telesales.html")
