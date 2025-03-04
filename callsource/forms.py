from django import forms

from .models import CallSource


class CallSourceForm(forms.ModelForm):
    class Meta:
        model = CallSource
        fields = ["name_call_source", "note", "category"]


class UploadCSVForm(forms.Form):
    file = forms.FileField()
    callsource_id = forms.IntegerField(required=True)
