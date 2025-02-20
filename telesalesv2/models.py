from django.db import models


class Customer(models.Model):
    customer_name = models.CharField(max_length=255)
    loan_account_number = models.CharField(max_length=50, unique=True)
    loan_id = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    family_phone = models.CharField(max_length=15, blank=True, null=True)
    current_address = models.TextField(blank=True, null=True)
    current_city = models.CharField(max_length=100, blank=True, null=True)
    current_area = models.CharField(max_length=100, blank=True, null=True)
    id_card = models.CharField(max_length=20, unique=True)
    product = models.CharField(max_length=100, blank=True, null=True)
    total_overdue = models.IntegerField(default=0)
    mob = models.IntegerField(default=0)
    tenor = models.IntegerField(default=0)
    assigned_date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "Khách hàng"
        verbose_name_plural = "Danh sách khách hàng"

    def __str__(self):
        return self.customer_name


class Campaign(models.Model):
    name = models.CharField(max_length=255)
    group = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Chiến dịch"
        verbose_name_plural = "Danh sách chiến dịch"

    def __str__(self):
        return self.name


class CampaignData(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="campaign_data")
    campaign = models.ForeignKey(
        Campaign, on_delete=models.CASCADE, related_name="campaign_data")
    agent = models.CharField(max_length=255, blank=True, null=True)
    spouse_phone = models.CharField(max_length=15, blank=True, null=True)
    additional_phone_1 = models.CharField(max_length=15, blank=True, null=True)
    additional_phone_2 = models.CharField(max_length=15, blank=True, null=True)
    active = models.BooleanField(default=True)
    call_status = models.CharField(max_length=50, blank=True, null=True)
    call_outcome_sub = models.CharField(max_length=255, blank=True, null=True)
    final_date = models.DateField(blank=True, null=True)
    last_action_time = models.DateTimeField(blank=True, null=True)
    last_action_code = models.CharField(max_length=50, blank=True, null=True)
    last_remark = models.TextField(blank=True, null=True)
    reference_phone_1 = models.CharField(max_length=15, blank=True, null=True)
    reference_phone_2 = models.CharField(max_length=15, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    call_count = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Chiến dịch data"
        verbose_name_plural = "Danh sách chiến dịch data"

    def __str__(self):
        return f"Data for {self.customer.customer_name} in {self.campaign.name}"
