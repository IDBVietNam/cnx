from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from home.forms.contact_info_form import ContactInfoForm


def contact_info_form(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ContactInfoForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(
                        request, f"{form.fields[field].label or field}: {error}"
                    )
    else:
        form = ContactInfoForm()  # Initialize an empty form
    context = {
        "form": form,
        "active_tab": "contact-info",
    }
    return render(request, "home/components/forms/contact-info-form.html", context)
