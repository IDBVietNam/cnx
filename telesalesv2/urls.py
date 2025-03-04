from django.urls import path

from . import views

app_name = "telesales"

urlpatterns = [
    path("telesales/", views.telesales, name="telesales-page"),
    path("filter-telesales/", views.filter_telesales, name="filter-telesales"),
]
