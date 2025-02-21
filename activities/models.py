import uuid

from django.db import models

from cnx_service.model import BaseModel


# Create your models here.
class Activities(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Foreign key to the User table
    created_by = models.CharField(max_length=255, null=True, blank=True)

    # Foreign key to the User table
    modified_by = models.CharField(max_length=255, null=True, blank=True)
    contract_number = models.CharField(max_length=255, null=True, blank=True)

    # Foreign key to the Calls table
    call_id = models.CharField(max_length=255, null=True, blank=True)

    # Foreign key to the Customer table
    customer_name = models.CharField(max_length=255, null=True, blank=True)
    agent = models.CharField(max_length=255, null=True, blank=True)
    contacted_person = models.CharField(max_length=255, null=True, blank=True)
    action_code = models.CharField(max_length=255, null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Activity"
        verbose_name_plural = "Activities"
