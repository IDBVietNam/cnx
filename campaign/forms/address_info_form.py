from django import forms

from campaign.models.address_info import AddressInfo


class AddressInfoForm(forms.ModelForm):
    permanent_address = forms.CharField(required=True, label="Địa chỉ thường trú")
    temporary_address = forms.CharField(required=False, label="Địa chỉ tạm trú")
    region = forms.CharField(required=False, label="Vùng")
    district = forms.CharField(required=False, label="Quận/Huyện")
    province = forms.CharField(required=False, label="Tỉnh")

    class Meta:
        model = AddressInfo
        fields = "__all__"
