from django.db import models

from cnx_service.model import BaseModel


class PhoneInfo(BaseModel):
    spouse_name = models.CharField(max_length=300)
    contact_name_1 = models.CharField(max_length=300)
    contact_relationship_1 = models.CharField(max_length=300)
    contact_name_2 = models.CharField(max_length=300)
    contact_relationship_2 = models.CharField(max_length=300)
    family_book = models.CharField(max_length=300)
    other_contact_name = models.CharField(max_length=300)
    other_contact_name_2 = models.CharField(max_length=300)

    class Meta:
        db_table = "phone_info"  # Explicitly setting the table name
