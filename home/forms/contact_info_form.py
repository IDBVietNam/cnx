from django import forms

from home.models.contact_info import ContactInfo


class ContactInfoForm(forms.ModelForm):
    loan_id = forms.CharField(required=False, label="Loan ID")
    contract_number = forms.CharField(required=True, label="Số hợp đồng")
    contract_date = forms.DateField(required=False, label="Contract Date")
    current_account = forms.CharField(required=False, label="Current Account")
    dpd_current = forms.IntegerField(required=False, label="DPD Current")
    dpd_assign = forms.IntegerField(label="DPD Assign")
    mob = forms.IntegerField(required=False, label="MOB")
    loan_amount = forms.CharField(required=True, label="Số tiền vay")
    loan_term = forms.IntegerField(required=True, label="Số kỳ hạn vay")
    obs_due_no = forms.IntegerField(required=False, label="OBS Due No")
    payment_request_date = forms.DateField(
        required=False, label="Ngày đề nghị thanh toán"
    )
    assign_invalid_date = forms.DateField(required=False, label="Assign Invalid Date")
    penalty_amount = forms.CharField(required=False, label="Số tiền phạt phát sinh")
    interest_amount = forms.CharField(required=False, label="Số tiền lãi phát sinh")
    principal_amount = forms.CharField(
        required=False, label="Số tiền nợ gốc đã phát sinh"
    )
    pos_assign = forms.CharField(required=False, label="POS Assign")
    total_payment = forms.CharField(required=True, label="Tổng số tiền thanh toán")
    last_result_final = forms.CharField(required=False, label="Last Result Final")
    total_amount = forms.CharField(required=False, label="Total_Amount")
    date_start = forms.DateField(required=False, label="Date Start")
    date_end = forms.DateField(required=False, label="Date End")
    late_days = forms.IntegerField(required=False, label="Số ngày trễ hạn")
    monthly_payment = forms.IntegerField(
        required=False, label="Số tiền phải đóng hàng tháng"
    )

    class Meta:
        model = ContactInfo
        fields = "__all__"
