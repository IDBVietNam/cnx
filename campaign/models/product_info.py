from django.db import models


class ProductInfo(models.Model):
    product = models.CharField(max_length=300)

    class Meta:
        db_table = "product_info"  # Explicitly setting the table name
