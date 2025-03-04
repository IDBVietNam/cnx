import os

import pandas as pd
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from callsource.forms import CallSourceForm, UploadCSVForm
from callsource.models import CallSource, HistoryCallSource
from cnx_service import settings


def callsource(request: HttpRequest) -> HttpResponse:
    if not request.headers.get("HX-Request"):
        return redirect("base:404")
    callsources = CallSource.objects.all()
    return render(
        request,
        "home/callsource/callsource.html",
        {"callsources": callsources},
    )


def callsource_create(request):
    if request.method == "POST":
        form = CallSourceForm(request.POST)
        if form.is_valid():
            _ = form.save()

            callsources = CallSource.objects.all()
            return render(
                request,
                "home/callsource/partials/callsource_list.html",
                {"callsources": callsources},
            )

        return JsonResponse({"success": False, "errors": form.errors})

    form = CallSourceForm()
    return render(
        request, "home/callsource/modal/callsource_modal.html", {"form": form}
    )


def upload_csv(request):
    if request.method == "POST":
        form = UploadCSVForm(request.POST, request.FILES)
        print("post", request.POST)
        if form.is_valid():
            file = request.FILES["file"]
            callsource_id = form.cleaned_data["callsource_id"]
            try:
                callsource = CallSource.objects.get(id=callsource_id)
            except CallSource.DoesNotExist:
                return JsonResponse(
                    {"success": False, "error": "CallSource not found"}, status=400
                )
            file_path = os.path.join(settings.MEDIA_ROOT, "uploads", file.name)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, "wb+") as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            try:
                if file.name.endswith(".csv"):
                    df = pd.read_csv(file_path)
                elif file.name.endswith(".xlsx"):
                    df = pd.read_excel(file_path, engine="openpyxl")
                else:
                    return JsonResponse(
                        {"success": False, "error": "Invalid file format"}, status=400
                    )
                print("DataFrame loaded:\n", df.head())

                total_rows = len(df)
                valid_mobile_rows = (
                    df["CUSTOMER_MOBILE_NUM"]
                    .dropna()
                    .astype(str)
                    .str.strip()
                    .ne("")
                    .sum()
                )
                callsource.total_customers = valid_mobile_rows
                callsource.save()
                failed_uploads = total_rows - valid_mobile_rows

                HistoryCallSource.objects.create(
                    completed_at=timezone.now(),
                    source=callsource,
                    uploader="admin",
                    status="completed",
                    total_uploaded=total_rows,
                    successful_uploads=valid_mobile_rows,
                    failed_uploads=failed_uploads,
                    file_name=file_path,
                )

            except Exception as e:
                return JsonResponse({"success": False, "error": str(e)}, status=500)

            return JsonResponse(
                {"success": True, "message": "File uploaded successfully!"}
            )

    else:
        form = UploadCSVForm()

        callsources = CallSource.objects.all()
        return render(
            request,
            "home/callsource/modal/callsource_modal_upload.html",
            {"form": form, "callsources": callsources},
        )


def history_callsource(request: HttpRequest, callsource_id: int) -> HttpResponse:
    if not request.headers.get("HX-Request"):
        return redirect("base:404")
    history_callsources = HistoryCallSource.objects.filter(source_id=callsource_id)
    return render(
        request,
        "home/callsource/modal/history_callsource_modal.html",
        {"historycallsources": history_callsources},
    )


def edit_callsource(request: HttpRequest, callsource_id: int) -> HttpResponse:
    if not request.headers.get("HX-Request"):
        return redirect("base:404")

    callsource = get_object_or_404(CallSource, id=callsource_id)

    return render(
        request,
        "home/callsource/modal/edit_callsource_modal.html",
        {"callsource": callsource},
    )


def update_callsource(request: HttpRequest, callsource_id: int) -> HttpResponse:
    if request.method == "POST":
        callsource = get_object_or_404(CallSource, id=callsource_id)
        callsource.name_call_source = request.POST.get("name_call_source")
        callsource.total_customers = request.POST.get("total_customers")
        callsource.save()
        callsources = CallSource.objects.all()

        response = render(
            request,
            "home/callsource/partials/callsource_list.html",
            {"callsources": callsources},
        )
        response["HX-Trigger"] = "closeModal"

        return response
