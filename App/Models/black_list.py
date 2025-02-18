import uuid
from django.db import models
from cnx_service.model import BaseModel

class BlackList(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    createdBy = models.CharField(max_length=255, null=True, blank=True)
    createdByName = models.CharField(max_length=255, null=True, blank=True)
    modifiedBy = models.CharField(max_length=255, null=True, blank=True)
    modifiedByName = models.CharField(max_length=255, null=True, blank=True)
    c_nguon = models.TextField(null=True, blank=True)
    c_ngayNhap = models.TextField(null=True, blank=True)
    c_phone = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Black_list"
        verbose_name_plural = "Black_lists"