from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from campaign.forms.product_info_form import ProductInfoForm


def product_info_form(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ProductInfoForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(
                        request, f"{form.fields[field].label or field}: {error}"
                    )
    else:
        form = ProductInfoForm()  # Initialize an empty form

    context = {
        "form": form,
        "active_tab": "product-info",
    }

    return render(request, "home/components/forms/product-info-form.html", context)
