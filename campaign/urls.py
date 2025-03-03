from django.urls import path

from campaign.views.address_info_form import address_info_form
from campaign.views.base_views import index
from campaign.views.call_outcome_form import call_outcome_form
from campaign.views.campaign_views import manage_telesales_campaign
from campaign.views.contact_info_form import contact_info_form
from campaign.views.cutomer_info_form import customer_info_form
from campaign.views.paymeny_info_form import payment_info_form
from campaign.views.phone_info_form import phone_info_form
from campaign.views.product_info_form import product_info_form

app_name = "campaign"

urlpatterns = [
    path("index/", index, name="index"),
    path(
        "manage-telesales/campaign/",
        manage_telesales_campaign,
        name="manage-telesales-campaign",
    ),
    path(
        "manage-telesales/campaign/customer_info/",
        customer_info_form,
        name="customer-info-form",
    ),
    path(
        "manage-telesales/campaign/contact_info/",
        contact_info_form,
        name="contact-info-form",
    ),
    path(
        "manage-telesales/campaign/address_info/",
        address_info_form,
        name="address-info-form",
    ),
    path(
        "manage-telesales/campaign/payment_info/",
        payment_info_form,
        name="payment-info-form",
    ),
    path(
        "manage-telesales/campaign/product_info/",
        product_info_form,
        name="product-info-form",
    ),
    path(
        "manage-telesales/campaign/call_outcome/",
        call_outcome_form,
        name="call-outcome-form",
    ),
    path(
        "manage-telesales/campaign/history_all/",
        product_info_form,
        name="history-all-form",
    ),
    path(
        "manage-telesales/campaign/history_limit/",
        product_info_form,
        name="history-limit-form",
    ),
    path(
        "manage-telesales/campaign/phone_info/", phone_info_form, name="phone-info-form"
    ),
]
