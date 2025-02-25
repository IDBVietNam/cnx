from django.db import models

from cnx_service.model import BaseModel


class CallOutcome(BaseModel):
    pds = models.BooleanField()
    final = models.BooleanField()
    contacted_person = models.CharField(max_length=300)
    action_code = models.CharField(max_length=300)
    reason_code = models.CharField(max_length=300)
    note = models.TextField(max_length=300)
    payment_date = models.DateField()
    payment_amount = models.IntegerField()

    class Meta:
        db_table = "call_outcome"  # Explicitly setting the table name
