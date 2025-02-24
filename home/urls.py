from django.urls import path

from home.views.base_views import index
from home.views.campaign_views import manage_telesales_campaign
from home.views.contact_info_form import contact_info_form
from home.views.cutomer_info_form import customer_info_form
from home.views.form_views import (
    address_info_form,
    payment_info_form,
    phone_info_form,
    product_info_form,
)

app_name = "home"

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
        "manage-telesales/campaign/phone_info/", phone_info_form, name="phone-info-form"
    ),
]
