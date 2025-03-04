from django.conf.urls.static import static
from django.urls import path

from callsource.views import (
    callsource,
    callsource_create,
    edit_callsource,
    history_callsource,
    update_callsource,
    upload_csv,
)
from cnx_service import settings

app_name = "callsources"

urlpatterns = [
    path("callsources/", callsource, name="callsources"),
    path("callsource/create/", callsource_create, name="callsource_create"),
    path("upload/", upload_csv, name="upload_csv"),
    path(
        "callsource/history/<int:callsource_id>/",
        history_callsource,
        name="historycallsource",
    ),
    path(
        "callsource/edit/<int:callsource_id>/", edit_callsource, name="editcallsource"
    ),
    path(
        "callsource/update/<int:callsource_id>/",
        update_callsource,
        name="updatecallsource",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
