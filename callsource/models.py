from django.db import models

from cnx_service.model import BaseModel


# Create your models here.
class CallSource(BaseModel):
    CATEGORY_CHOICES = [
        ("hotline", "Hotline"),
        ("community", "Community"),
        ("digital", "Digital"),
        ("crm_age", "CRM Age"),
        ("retention", "Retention"),
        ("etc", "ETC"),
        ("referral", "Referral"),
    ]

    name_call_source = models.CharField(max_length=255, null=True, blank=True)
    total_customers = models.IntegerField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    category = models.CharField(
        max_length=50, choices=CATEGORY_CHOICES, null=True, blank=True
    )
    create_by = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "CallSource"
        verbose_name_plural = "CallSources"
        db_table = "call_source"
