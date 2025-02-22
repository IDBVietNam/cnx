from django.urls import path

from .views import custom_404_view

app_name = "base"

urlpatterns = [path("404/", custom_404_view, name="404")]
