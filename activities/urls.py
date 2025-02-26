from django.urls import path

from activities.views import activities_form, test_telesales

app_name = "activities"

urlpatterns = [
    path("index/", activities_form, name="activities_form"),
    path("test-telesales/", test_telesales, name="test-telesales"),
]
