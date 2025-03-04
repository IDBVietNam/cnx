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


class HistoryCallSource(BaseModel):
    completed_at = models.DateTimeField(null=True, blank=True)
    uploader = models.CharField(max_length=255)
    source = models.ForeignKey(
        CallSource, on_delete=models.CASCADE, related_name="history_sources"
    )
    status = models.CharField(max_length=50)
    total_uploaded = models.IntegerField()
    successful_uploads = models.IntegerField()
    failed_uploads = models.IntegerField()
    file_name = models.CharField(max_length=255, verbose_name="Uploaded File")

    class Meta:
        db_table = "history_call_source"
