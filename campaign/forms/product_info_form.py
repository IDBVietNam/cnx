from django import forms

from campaign.models.product_info import ProductInfo


class ProductInfoForm(forms.ModelForm):
    product = forms.CharField(required=False)

    class Meta:
        model = ProductInfo
        fields = "__all__"
