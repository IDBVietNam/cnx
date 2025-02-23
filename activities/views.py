from django.core.paginator import Paginator
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
    page_number = request.GET.get("page", 1)  # Lấy số trang từ query parameter
    paginator = Paginator(activities, 1)  # 10 items mỗi trang
    page_obj = paginator.get_page(page_number)

    try:
        activities_page = paginator.page(page_number)
    except Exception:
        activities_page = paginator.page(1)  # Nếu lỗi, quay về trang đầu tiên

    return render(
        request,
        "home/activities/activities.html",
        {
            "activities": activities_page,
            "previous_page_number": page_obj.previous_page_number()
            if page_obj.has_previous()
            else None,
        },
    )
