from django.db import models
import uuid


class TelesalesV2(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)  # DateCreated
    mobile_number = models.CharField(
        max_length=15, blank=True, null=True)  # Di động
    reference_phone_1 = models.CharField(
        max_length=15, blank=True, null=True)  # SDT Ref 1
    reference_phone_2 = models.CharField(
        max_length=15, blank=True, null=True)  # SDT Ref 2
    spouse_phone = models.CharField(
        max_length=15, blank=True, null=True)  # Spousephone
    additional_phone_1 = models.CharField(
        max_length=15, blank=True, null=True)  # Add phone 1
    additional_phone_2 = models.CharField(
        max_length=15, blank=True, null=True)  # Add phone 2
    serial_number = models.CharField(max_length=20, unique=True)  # STT
    assigned_agent = models.CharField(max_length=50)  # Nhân viên phụ trách
    contract_number = models.CharField(
        max_length=50, unique=True)  # Số hợp đồng
    # ID Hợp đồng (Chứa thông tin SHD, KH, CCCD, Nợ,...)
    contract_info = models.TextField()
    call_source = models.CharField(max_length=100)  # Nguồn gọi
    customer_code = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)  # UUID thay thế c_fkKH
    title = models.CharField(max_length=255, blank=True, null=True)  # Tiêu đề
    id_card_number = models.CharField(
        max_length=20, unique=True)  # Số CMND (CCCD)

    customer_name = models.CharField(max_length=255)  # Tên KH
    total_overdue = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True, null=True)  # Total Overdue
    tenor = models.CharField(max_length=50, blank=True, null=True)  # Tenor
    product_group = models.CharField(
        max_length=50, blank=True, null=True)  # PRODUCT_GROUP
    full_address = models.TextField(blank=True, null=True)  # Địa chỉ đầy đủ
    district = models.CharField(
        max_length=100, blank=True, null=True)  # Quận/Huyện
    city = models.CharField(max_length=100, blank=True,
                            null=True)  # Tỉnh/Thành Phố
    call_status = models.CharField(
        max_length=50, blank=True, null=True)  # Trạng thái gọi
    recall_time = models.DateTimeField(
        blank=True, null=True)  # Thời gian gọi lại
    call_result = models.CharField(
        max_length=100, blank=True, null=True)  # Kết quả gọi
    call_reason = models.TextField(blank=True, null=True)  # Lý do gọi
    scheduled_time = models.DateTimeField(
        blank=True, null=True)  # Thời gian chỉ định
    c_stt = models.AutoField(primary_key=True)  # c_stt tự tăng
    date_final = models.DateTimeField(blank=True, null=True)  # Date final
    last_action_time = models.DateTimeField(
        blank=True, null=True)  # Last action time
    last_action_code = models.CharField(
        max_length=50, blank=True, null=True)  # Last action code
    last_remark = models.TextField(blank=True, null=True)  # Last remark
    call_source_uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)  # c_nguon (UUID)

    def __str__(self):
        return f"{self.contract_number} - {self.customer_name}"
