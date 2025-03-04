from django import forms

from campaign.models.call_outcome import CallOutcome


class CallOutcomeForm(forms.ModelForm):
    pds = forms.BooleanField(required=False, label="Trả PDS")
    note = forms.Textarea()
    payment_date = forms.DateField(required=False, label="Ngày hứa thanh toán")
    payment_amount = forms.IntegerField(required=False, label="Số tiền hứa thanh toán")

    class Meta:
        model = CallOutcome
        fields = "__all__"
