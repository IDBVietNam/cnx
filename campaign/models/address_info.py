from django.db import models

from cnx_service.model import BaseModel


class AddressInfo(BaseModel):
    permanent_address = models.CharField(max_length=500)
    temporary_address = models.CharField(max_length=500)
    region = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    district = models.CharField(max_length=100)

    class Meta:
        db_table = "address_info"  # Explicitly setting the table name
