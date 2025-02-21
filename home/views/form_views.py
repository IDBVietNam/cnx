from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from home.forms.customer_info_form import CustomerInfoForm
from home.models.customer_info import CustomerInfo


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
        messages.error(request, "Validation error")

        if form.is_valid():
            form.save(commit=False)  # Create instance without saving
            # Perform additional logic here if needed
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


def init_customer_info_data() -> CustomerInfo:
    return CustomerInfo(
        name="John Doe",
        gender="Male",
        id_number="123456789",
        day_of_birth="1990-01-01",
        family_relation="Brother",
        agency="Central Agency",
        contract_number="CN-00123",
        company_name="Tech Innovators Inc.",
        company_address="123 Innovation Drive",
        company_district="Central Business District",
        company_province="California",
        group="R&D",
    )
