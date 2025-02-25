from django.db import models

from cnx_service.model import BaseModel


# Create your models here.
class CallSource(BaseModel):
    name_call_source = models.CharField(max_length=255, null=True, blank=True)
    total_customers = models.IntegerField(null=True, blank=True)
    create_by = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "CallSource"
        verbose_name_plural = "CallSources"
        db_table = "call_source"
