import uuid
from django.db import models
from cnx_service.model import BaseModel

class CallStatus(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    createdBy = models.CharField(max_length=255, null=True, blank=True)
    createdByName = models.CharField(max_length=255, null=True, blank=True)
    modifiedBy = models.CharField(max_length=255, null=True, blank=True)
    modifiedByName = models.CharField(max_length=255, null=True, blank=True)
    c_label = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = "CallStatus"
        verbose_name_plural = "CallStatus"