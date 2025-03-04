from django.core.paginator import EmptyPage, Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from activities.filters import ActivitiesFilter
from activities.models import Activities


def filter_activities(request: HttpRequest) -> HttpResponse:
    if not request.headers.get("HX-Request"):
        return redirect("base:404")

    per_page = request.GET.get("per_page", "10")  # Default to "10"
    contract_number = request.GET.get("contract_number", "")
    action_code = request.GET.get("action_code", "")
    contacted_person = request.GET.get("contacted_person", "")
    from_date = request.GET.get("from_date", "")
    to_date = request.GET.get("to_date", "")

    # Apply filtering
    activities_filter = ActivitiesFilter(request.GET, queryset=Activities.objects.all())

    try:
        page_number = int(request.GET.get("page", 1))
        if page_number < 1:
            page_number = 1
    except ValueError:
        page_number = 1  # Default to 1 if invalid

    paginator = Paginator(activities_filter.qs, int(per_page))

    try:
        page_obj = paginator.get_page(page_number)
    except EmptyPage:
        page_obj = paginator.get_page(1)
    return render(
        request,
        "home/activities/partials/activities_table.html",
        {
            "activities": page_obj,
            "current_page": page_obj.number,
            "total_pages": paginator.num_pages,
            "per_page": per_page,
            "contract_number": contract_number,
            "action_code": action_code,
            "contacted_person": contacted_person,
            "from_date": from_date,
            "to_date": to_date,
        },
    )


def activities(request: HttpRequest) -> HttpResponse:
    if not request.headers.get("HX-Request"):
        return redirect("base:404")

    activities_filter = ActivitiesFilter(request.GET, queryset=Activities.objects.all())

    page_number = request.GET.get("page", 1)
    per_page = request.GET.get("per_page", 10)

    paginator = Paginator(activities_filter.qs, per_page)
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "home/activities/activities.html",
        {
            "activities": page_obj,
            "current_page": page_obj.number,
            "total_pages": paginator.num_pages,
            "per_page": per_page,
            "filter": activities_filter,  # Pass filter for UI
        },
    )


def test_telesales(request: HttpRequest) -> HttpResponse:
    if not request.headers.get("HX-Request"):
        return redirect("base:404")
    return render(request, "home/activities/test_telesales.html")
