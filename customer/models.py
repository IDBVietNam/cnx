from django.db import models

from cnx_service.model import BaseModel


class Customer(BaseModel):
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    dob = models.DateField()
    total_overdue = models.FloatField(blank=True, null=False, default=0)
    tenor = models.CharField(max_length=50, blank=True)
    mob = models.CharField(max_length=255, blank=True)
    identity_card = models.CharField(max_length=255, blank=True)
    loan_account_no = models.CharField(max_length=255, blank=True)
    loan_information = models.TextField(blank=True)
    moible_phone = models.CharField(max_length=12, blank=True)
    family_phone = models.CharField(max_length=12, blank=True)
    product_group = models.CharField(max_length=50)
    current_full_address = models.TextField()
