from django.db import models

from cnx_service.model import BaseModel


class PaymentInfo(BaseModel):
    first_paid_date = models.DateField()
    account_number = models.CharField(max_length=100)
    largest_amount = models.DecimalField(max_digits=12, decimal_places=2)
    last_payment_date = models.DateField()
    disbursement_date = models.DateField()
    cif = models.CharField(max_length=100)
    due_date_overdue = models.DateField()
    next_due_date = models.DateField()
    next_due_amount = models.DecimalField(max_digits=12, decimal_places=2)
    future_prin_amt = models.DecimalField(max_digits=12, decimal_places=2)
    remain_prin = models.DecimalField(max_digits=12, decimal_places=2)
    pos_bom = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        db_table = "payment_info"  # Explicitly setting the table name

    def __str__(self):
        return self.account_number
