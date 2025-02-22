from django.urls import path

from activities.views import activities, filter_activities

app_name = "activities"

urlpatterns = [
    path("activities/", activities, name="activities-page"),
    path("filter-activities/", filter_activities, name="filter-activities"),
]
