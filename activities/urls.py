from django.urls import path

from activities.views import activities, filter_activities, test_telesales

app_name = "activities"

urlpatterns = [
    path("activities/", activities, name="activities-page"),
    path("filter-activities/", filter_activities, name="filter-activities"),
    path("test-telesales/", test_telesales, name="test-telesales"),
]
