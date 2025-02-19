# from django import forms

# from home.models.customer_info import CustomerInfo

# class CustomerInfoForm(forms.ModelForm):
#     name = forms.CharField(required=False, label="Tên KH")
#     id_number = forms.CharField(max_length=20, label="CCCD")
#     day_of_birth = forms.DateField(label="Ngày sinh", required=False)
#     gender = forms.CharField(label="Giới tính", required=False)
#     contract_number = forms.CharField(label="Số hợp đồng", required=False)
#     company_name = forms.CharField(label="Tên công ty", required=False)
#     company_address = forms.CharField(label="Địa chỉ công ty", required=False)
#     company_district = forms.CharField(label="Địa chỉ công ty - Quận/Huyện", required=False)
#     company_province = forms.CharField(label="Địa chỉ công ty - Tỉnh/TP", required=False)

#     class Meta:
#         model = CustomerInfo
#         fields = '__all__'

from django import forms

from home.models.customer_info import CustomerInfo


class CustomerInfoForm(forms.Form):
    name = forms.CharField(required=False, label="Tên KH")
    id_number = forms.CharField(max_length=20, label="CCCD")
    day_of_birth = forms.DateField(label="Ngày sinh", required=True)
    gender = forms.CharField(label="Giới tính", required=False)
    contract_number = forms.CharField(label="Số hợp đồng", required=False)
    company_name = forms.CharField(label="Tên công ty", required=False)
    company_address = forms.CharField(label="Địa chỉ công ty", required=True)
    company_district = forms.CharField(
        label="Địa chỉ công ty - Quận/Huyện", required=False
    )
    company_province = forms.CharField(
        label="Địa chỉ công ty - Tỉnh/TP", required=False
    )

    def save(self, commit=True):
        data = self.cleaned_data
        customer_info = CustomerInfo(**data)
        return customer_info
