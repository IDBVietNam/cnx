from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from home.forms.customer_info_form import CustomerInfoForm


def customer_info_form(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CustomerInfoForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(
                        request, f"{form.fields[field].label or field}: {error}"
                    )
    else:
        form = CustomerInfoForm()  # Initialize an empty form

    context = {
        "form": form,
        "active_tab": "customer-info",
        "gender_options": [
            {"value": "Male", "label": "Nam"},
            {"value": "Female", "label": "Nữ"},
            {"value": "Other", "label": "Khác"},
        ],
    }

    return render(request, "home/components/forms/customer-info-form.html", context)
