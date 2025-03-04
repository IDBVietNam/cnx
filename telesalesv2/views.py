from django.core.paginator import EmptyPage, Paginator
from django.db.models import CharField
from django.db.models.functions import Cast
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .filters import TelesalesV2Filter
from .models import TelesalesV2


def filter_telesales(request: HttpRequest) -> HttpResponse:
    if not request.headers.get("HX-Request"):
        return redirect("base:404")

    default_items_per_page = 10

    telesalesV2_filter = TelesalesV2Filter(
        request.GET, queryset=TelesalesV2.objects.all()
    )

    default_page_number = 1
    try:
        page_number = int(request.GET.get("page", 1))
        if page_number < 1:
            page_number = 1
    except ValueError:
        page_number = default_page_number

    paginator = Paginator(telesalesV2_filter.qs, default_items_per_page)

    try:
        page_obj = paginator.get_page(page_number)
    except EmptyPage:
        page_obj = paginator.get_page(1)

    return render(
        request,
        "telesalesv2/partials/telesales_table.html",
        {
            "telesales": page_obj,
            "current_page": page_obj.number,
            "total_pages": paginator.num_pages,
            # "contract_number": contract_number,
            # "action_code": action_code,
            # "contacted_person": contacted_person,
            # "from_date": from_date,
            # "to_date": to_date,
        },
    )


def telesales(request):
    sales = TelesalesV2.objects.all()

    contract_number = request.GET.get("contract_number", "")
    contract_info = request.GET.get("contract_info", "")
    assigned_agent = request.GET.get("assigned_agent", "")
    call_id = request.GET.get("call_id", "")
    id_card_number = request.GET.get("id_card_number", "")
    mobile_number = request.GET.get("mobile_number", "")
    call_reason = request.GET.get("call_reason", "")
    call_status = request.GET.get("call_status", "")
    scheduled_time = request.GET.get("scheduled_time", "").strip()

    if scheduled_time:
        sales = sales.annotate(
            scheduled_time_str=Cast("scheduled_time", CharField())
        ).filter(scheduled_time_str__contains=scheduled_time)

    if call_status:
        sales = sales.filter(call_status=call_status)

    if call_reason:
        sales = sales.filter(call_reason__icontains=call_reason)

    if mobile_number:
        sales = sales.filter(mobile_number__icontains=mobile_number)

    if id_card_number:
        sales = sales.filter(id_card_number__icontains=id_card_number)
    if call_id:
        sales = sales.filter(id__icontains=call_id)
    if contract_number:
        sales = sales.filter(contract_number__icontains=contract_number)
    if contract_info:
        sales = sales.filter(contract_info__icontains=contract_info)
    if assigned_agent:
        sales = sales.filter(assigned_agent__icontains=assigned_agent)

    items_per_page = 1
    page_number = request.GET.get("page", 1)

    paginator = Paginator(sales, items_per_page)
    page_obj = paginator.get_page(page_number)

    context = {
        "telesales": page_obj,
        "page_obj": page_obj,
        "CALL_STATUS_CHOICES": TelesalesV2.CALL_STATUS_CHOICES,
        "CALL_RESULT_CHOICES": TelesalesV2.CALL_RESULT_CHOICES,
        "contract_number": contract_number,
        "call_id": call_id,
        "assigned_agent": assigned_agent,
        "call_status": call_status,
    }
    return render(request, "telesalesv2/telesales.html", context)
