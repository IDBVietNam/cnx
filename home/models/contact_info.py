from django.db import models

from cnx_service.model import BaseModel


class ContactInfo(BaseModel):
    penalty_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_amount = models.DecimalField(max_digits=12, decimal_places=2)
    principal_amount = models.DecimalField(max_digits=12, decimal_places=2)
    pos_assign = models.DecimalField(max_digits=12, decimal_places=2)
    last_result_final = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    date_start = models.DateField()
    date_end = models.DateField()
    total_payment = models.DecimalField(max_digits=12, decimal_places=2)
    assign_invalid_date = models.DateField()
    payment_request_date = models.DateField()
    obs_due_no = models.IntegerField()
    loan_term = models.IntegerField()
    loan_amount = models.DecimalField(max_digits=12, decimal_places=2)
    mob = models.IntegerField()
    dpd_assign = models.IntegerField()
    dpd_current = models.IntegerField()
    current_account = models.CharField(max_length=100)
    contract_date = models.DateField()
    contract_number = models.CharField(max_length=100)
    loan_id = models.CharField(max_length=100)
    late_days = models.IntegerField(default=0)
    monthly_payment = models.IntegerField(default=0)

    class Meta:
        db_table = "contact_info"  # Explicitly setting the table name
