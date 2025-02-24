from django import forms

from campaign.models.phone_info import PhoneInfo


class PhoneInfoForm(forms.ModelForm):
    spouse_name = forms.CharField(required=False, label="Tên Vợ/Chồng")
    contact_name_1 = forms.CharField(required=False, label="Liên hệ thứ 1")
    contact_relationship_1 = forms.CharField(
        required=False, label="Mối quan hệ của SDT thứ 1"
    )
    contact_name_2 = forms.CharField(required=False, label="Liên hệ thứ 2")
    contact_relationship_2 = forms.CharField(
        required=False, label="Mối quan hệ của SDT thứ 2"
    )
    family_book = forms.CharField(required=False, label="Family Book")
    other_contact_name = forms.CharField(required=False, label="Tên liên hệ khác")
    other_contact_name_2 = forms.CharField(required=False, label="Tên liên hệ khác 2")

    class Meta:
        model = PhoneInfo
        fields = "__all__"
