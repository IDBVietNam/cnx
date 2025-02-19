from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return render(request, "phoenix_example/index.html")


def component_accordion(request: HttpRequest) -> HttpResponse:
    return render(request, "phoenix_example/component/accordion.html")
