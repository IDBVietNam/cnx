from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from activities.filters import ActivityFilter
from activities.models import Activities


def filter_activities(request: HttpRequest) -> HttpResponse:
    if not request.headers.get("HX-Request"):
        return redirect("base:404")
    activity_filter = ActivityFilter(request.GET, queryset=Activities.objects.all())
    return render(
        request,
        "home/activities/partials/activities_list.html",
        {"activities": activity_filter.qs},
    )


def activities(request: HttpRequest) -> HttpResponse:
    if not request.headers.get("HX-Request"):
        return redirect("base:404")
    activities = Activities.objects.all()
    return render(
        request,
        "home/activities/activities.html",
        {"activities": activities},
    )
