from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from campaign.forms.address_info_form import AddressInfoForm


def address_info_form(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = AddressInfoForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(
                        request, f"{form.fields[field].label or field}: {error}"
                    )
    else:
        form = AddressInfoForm()  # Initialize an empty form
    context = {
        "form": form,
        "active_tab": "address-info",
    }
    return render(request, "home/components/forms/address-info-form.html", context)
