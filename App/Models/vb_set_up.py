import uuid
from django.db import models
from cnx_service.model import BaseModel

class VBSetup(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    createdBy = models.CharField(max_length=255, null=True, blank=True)
    createdByName = models.CharField(max_length=255, null=True, blank=True)
    modifiedBy = models.CharField(max_length=255, null=True, blank=True)
    modifiedByName = models.CharField(max_length=255, null=True, blank=True)
    c_GoiLaiNeuNgheMayItHon = models.TextField(null=True, blank=True)
    c_Channel = models.TextField(null=True, blank=True)
    c_ThoiGianGoiLaiToiThieu = models.TextField(null=True, blank=True)
    c_status = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = "VBSetup"
        verbose_name_plural = "VBSetup"