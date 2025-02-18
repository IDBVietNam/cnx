import uuid
from django.db import models
from cnx_service.model import BaseModel

class Queue(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    createdBy = models.CharField(max_length=255, null=True, blank=True)
    createdByName = models.CharField(max_length=255, null=True, blank=True)
    modifiedBy = models.CharField(max_length=255, null=True, blank=True)
    modifiedByName = models.CharField(max_length=255, null=True, blank=True)
    c_queue_name = models.TextField()
    
    class Meta:
        verbose_name = "Queue"
        verbose_name_plural = "Queues"
