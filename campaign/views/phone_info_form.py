from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from campaign.forms.phone_info_form import PhoneInfoForm


def phone_info_form(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = PhoneInfoForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(
                        request, f"{form.fields[field].label or field}: {error}"
                    )
    else:
        form = PhoneInfoForm()  # Initialize an empty form
    context = {
        "form": form,
        "active_tab": "phone-info",
    }
    return render(request, "home/components/forms/phone-info-form.html", context)
