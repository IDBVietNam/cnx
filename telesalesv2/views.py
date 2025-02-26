from django.core.paginator import Paginator
from django.db.models import CharField
from django.db.models.functions import Cast
from django.shortcuts import render

from .models import TelesalesV2


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

    per_page = 1
    page_number = request.GET.get("page", 1)  # Lấy số trang từ URL

    # Tạo Paginator
    paginator = Paginator(sales, per_page)
    page_obj = paginator.get_page(page_number)

    context = {
        "sales": page_obj.object_list,
        "page_obj": page_obj,
        "CALL_STATUS_CHOICES": TelesalesV2.CALL_STATUS_CHOICES,
        "CALL_RESULT_CHOICES": TelesalesV2.CALL_RESULT_CHOICES,
        "contract_number": contract_number,
        "call_id": call_id,
        "assigned_agent": assigned_agent,
        "call_status": call_status,
    }
    return render(request, "telesalesv2/telesales.html", context)
