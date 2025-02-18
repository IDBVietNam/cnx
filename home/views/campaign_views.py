from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def manage_telesales_campaign(request: HttpRequest) -> HttpResponse:
    tabs = [
        {"id": "customer-info", "label": "Customer Info", "url": "home:customer-info-form"},
        {"id": "contact-info", "label": "Contact Info", "url": "home:contact-info-form"},
        {"id": "payment-info", "label": "Payment Info", "url": "home:payment-info-form"},
        {"id": "product-info", "label": "Product Info", "url": "home:product-info-form"},
        {"id": "address-info", "label": "Address Info", "url": "home:address-info-form"},
        {"id": "phone-info", "label": "Phone Info", "url": "home:phone-info-form"},
    ]
    return render(request, "home/manage_telesales/campaign.html", {"active": "manage_telesales_campaign", "tabs": tabs})
