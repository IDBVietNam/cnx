from django.db import models

from cnx_service.model import BaseModel


class ProductInfo(BaseModel):
    product = models.CharField(max_length=300)

    class Meta:
        db_table = "product_info"  # Explicitly setting the table name
