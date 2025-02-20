from django.db import models


class CustomerInfo(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=50)
    id_number = models.CharField(max_length=20, unique=True)
    day_of_birth = models.DateField()
    family_relation = models.CharField(max_length=255, blank=True, null=True)
    agency = models.CharField(max_length=255, blank=True, null=True)
    contract_number = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_address = models.CharField(max_length=255, blank=True, null=True)
    company_district = models.CharField(max_length=255, blank=True, null=True)
    company_province = models.CharField(max_length=255, blank=True, null=True)
    group = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
