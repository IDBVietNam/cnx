from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from callsource.models import CallSource


# Create your views here.
def callsource(request: HttpRequest) -> HttpResponse:
    if not request.headers.get("HX-Request"):
        return redirect("base:404")
    callsources = CallSource.objects.all()
    return render(
        request,
        "home/callsource/callsource.html",
        {"callsources": callsources},
    )
