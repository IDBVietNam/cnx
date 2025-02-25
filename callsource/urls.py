from django.urls import path

from callsource.views import callsource

app_name = "callsources"

urlpatterns = [path("callsources/", callsource, name="callsources")]
