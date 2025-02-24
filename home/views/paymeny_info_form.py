from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from home.forms.payment_info_form import PaymentInfoForm


def payment_info_form(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = PaymentInfoForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(
                        request, f"{form.fields[field].label or field}: {error}"
                    )
    else:
        form = PaymentInfoForm()  # Initialize an empty form

    context = {
        "form": form,
        "active_tab": "payment-info",
    }

    return render(request, "home/components/forms/payment-info-form.html", context)
