# from django.db import models

# class CustomerInfo():
#     name = models.CharField(max_length=255)
#     gender = models.CharField(max_length=50)
#     id_number = models.CharField(max_length=20, unique=True)
#     day_of_birth = models.DateField()
#     family_relation = models.CharField(max_length=255, blank=True, null=True)
#     agency = models.CharField(max_length=255, blank=True, null=True)
#     contract_number = models.CharField(max_length=100)
#     company_name = models.CharField(max_length=255, blank=True, null=True)
#     company_address = models.CharField(max_length=255, blank=True, null=True)
#     company_district = models.CharField(max_length=255, blank=True, null=True)
#     company_province = models.CharField(max_length=255, blank=True, null=True)
#     group = models.CharField(max_length=100, blank=True, null=True)

#     def __str__(self):
#         return self.name


# temporary class to simulate the model
class CustomerInfo:
    def __init__(
        self,
        name: str,
        gender: str,
        id_number: str,
        day_of_birth,
        family_relation: str = None,
        agency: str = None,
        contract_number: str = None,
        company_name: str = None,
        company_address: str = None,
        company_district: str = None,
        company_province: str = None,
        group: str = None,
    ):
        self.name = name
        self.gender = gender
        self.id_number = id_number
        self.day_of_birth = day_of_birth
        self.family_relation = family_relation
        self.agency = agency
        self.contract_number = contract_number
        self.company_name = company_name
        self.company_address = company_address
        self.company_district = company_district
        self.company_province = company_province
        self.group = group

    def __str__(self):
        return self.name
