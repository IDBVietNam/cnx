import uuid
from django.db import models
from cnx_service.model import BaseModel


class NguonGoi(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    createdBy = models.CharField(max_length=255, null=True, blank=True)
    createdByName = models.CharField(max_length=255, null=True, blank=True)
    modifiedBy = models.CharField(max_length=255, null=True, blank=True)
    modifiedByName = models.CharField(max_length=255, null=True, blank=True)
    c_phanLoai = models.TextField(null=True, blank=True)
    c_ghiChu = models.TextField(null=True, blank=True)
    c_label = models.TextField(null=True, blank=True)
    c_fkBrand = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = "nguon_goi"
        verbose_name_plural = "nguon_goi"
