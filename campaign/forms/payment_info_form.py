from django import forms

from campaign.models.payment_info import PaymentInfo


class PaymentInfoForm(forms.ModelForm):
    first_paid_date = forms.DateField(
        required=False, label="First Paid Date", input_formats=["%d/%m/%Y"]
    )
    account_number = forms.CharField(required=False, label="Số tài khoản")
    largest_amount = forms.CharField(
        required=False, label="Số tiền thanh toán gần nhất"
    )
    last_payment_date = forms.DateField(
        required=False, label="Ngày thanh toán gần nhất", input_formats=["%d/%m/%Y"]
    )
    disbursement_date = forms.DateField(
        required=False, label="Disbursement Date", input_formats=["%d/%m/%Y"]
    )
    cif = forms.CharField(required=False, label="CIF")
    due_date_overdue = forms.DateField(
        required=False, label="Due Date Overdue", input_formats=["%d/%m/%Y"]
    )
    next_due_date = forms.DateField(
        required=False,
        label="Ngày đến hạn chu kỳ tiếp theo",
        input_formats=["%d/%m/%Y"],
    )
    next_due_amount = forms.CharField(
        required=False, label="Số tiền phải đóng trong chu kỳ tiếp theo"
    )
    future_prin_amt = forms.CharField(required=False, label="Future PRIN AMT")
    remain_prin = forms.CharField(required=False, label="Remain PRIN")
    pos_bom = forms.CharField(required=False, label="POS bom")

    class Meta:
        model = PaymentInfo
        fields = "__all__"
