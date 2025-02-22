from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def custom_404_view(request: HttpRequest) -> HttpResponse:
    return render(request, "base/404.html", status=404)
