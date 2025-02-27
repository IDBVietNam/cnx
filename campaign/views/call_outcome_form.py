from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from campaign.forms.call_outcome_form import CallOutcomeForm


def call_outcome_form(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CallOutcomeForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(
                        request, f"{form.fields[field].label or field}: {error}"
                    )
    else:
        form = CallOutcomeForm()  # Initialize an empty form
    context = {
        "form": form,
        "active_tab": "call-outcome",
        "contacted_person_options": [
            {"value": "1", "label": "Test User"},
        ],
        "action_code_options": [
            {"value": "1", "label": "Action Code 1"},
            {"value": "2", "label": "Action Code 2"},
            {"value": "3", "label": "Action Code 3"},
        ],
        "reason_code_options": [
            {"value": "1", "label": "Reason Code 1"},
            {"value": "2", "label": "Reason Code 2"},
            {"value": "3", "label": "Reason Code 3"},
        ],
    }
    return render(request, "home/components/forms/call-outcome-form.html", context)
