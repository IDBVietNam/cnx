from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def manage_telesales_campaign(request: HttpRequest) -> HttpResponse:
    tabs = [
        {
            "id": "customer-info",
            "label": "Customer Info",
            "url": "campaign:customer-info-form",
        },
        {
            "id": "contact-info",
            "label": "Contact Info",
            "url": "campaign:contact-info-form",
        },
        {
            "id": "payment-info",
            "label": "Payment Info",
            "url": "campaign:payment-info-form",
        },
        {
            "id": "product-info",
            "label": "Product Info",
            "url": "campaign:product-info-form",
        },
        {
            "id": "address-info",
            "label": "Address Info",
            "url": "campaign:address-info-form",
        },
        {"id": "phone-info", "label": "Phone Info", "url": "campaign:phone-info-form"},
    ]
    right_tabs = [
        {
            "id": "call-outcome",
            "label": "Call Outcome",
            "url": "campaign:call-outcome-form",
        },
        {
            "id": "history-all",
            "label": "History All",
            "url": "campaign:history-all-form",
        },
        {
            "id": "history-limit",
            "label": "History Limit",
            "url": "campaign:history-limit-form",
        },
    ]
    return render(
        request,
        "home/manage_telesales/campaign.html",
        {"active": "manage_telesales_campaign", "tabs": tabs, "right_tabs": right_tabs},
    )
