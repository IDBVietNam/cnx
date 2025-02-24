from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def address_info_form(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "home/components/forms/address-info-form.html",
        {"active_tab": "address-info"},
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
