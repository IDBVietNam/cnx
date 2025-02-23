from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from home.forms.customer_info_form import CustomerInfoForm


def contact_info_form(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "home/components/forms/contact-info-form.html",
        {"active_tab": "contact-info"},
    )


def address_info_form(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "home/components/forms/address-info-form.html",
        {"active_tab": "address-info"},
    )


def payment_info_form(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "home/components/forms/payment-info-form.html",
        {"active_tab": "payment-info"},
    )


def product_info_form(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "home/components/forms/product-info-form.html",
        {"active_tab": "product-info"},
    )


def phone_info_form(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "home/components/forms/phone-info-form.html",
        {"active_tab": "phone-info"},
    )


def customer_info_form(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CustomerInfoForm(request.POST)

        if form.is_valid():
            form.save(commit=False)  # Create instance without saving
            # Perform additional logic here if needed
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{form.fields[field].label or field}: {error}")
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
