from django.urls import path

from activities.views import activities_form

app_name = "activities"

urlpatterns = [path("index/", activities_form, name="activities_form")]
