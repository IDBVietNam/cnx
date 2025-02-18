import uuid
from django.db import models
from cnx_service.model import BaseModel

class VBChienDich(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    createdBy = models.CharField(max_length=255, null=True, blank=True)
    createdByName = models.CharField(max_length=255, null=True, blank=True)
    modifiedBy = models.CharField(max_length=255, null=True, blank=True)
    modifiedByName = models.CharField(max_length=255, null=True, blank=True)
    c_SoLanGoiLai = models.TextField(null=True, blank=True)
    c_file = models.TextField(null=True, blank=True)
    c_Playback = models.TextField(null=True, blank=True)
    c_From = models.TextField(null=True, blank=True)
    c_To = models.TextField(null=True, blank=True)
    c_Subject = models.TextField(null=True, blank=True)
    c_status = models.TextField(null=True, blank=True)
    c_isVisible = models.TextField(null=True, blank=True)
    c_stt = models.IntegerField(unique=True)
    c_SoKenhToiDa = models.TextField(null=True, blank=True)
    c_poolnum = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = "VBChienDich"
        verbose_name_plural = "VBChienDich"