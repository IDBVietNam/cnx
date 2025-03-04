import uuid

from django.db import models

from cnx_service.model import BaseModel


class TelesalesV2(BaseModel):
    CALL_STATUS_CHOICES = [
        ("new", "New"),
        ("follow1", "Follow1"),
        ("follow2", "Follow2"),
        ("follow3", "Follow3"),
    ]

    CALL_RESULT_CHOICES = [
        ("brother", "Brother"),
        ("child", "Child"),
        ("client", "Client"),
        ("father", "Father"),
        ("mother", "Mother"),
        ("nobody", "Nobody"),
        ("other", "Other"),
        ("sibling", "Sibling"),
        ("sister", "Sister"),
        ("spouse", "Spouse"),
    ]
    reference_phone_1 = models.CharField(
        max_length=15, blank=True, verbose_name="SĐT Ref 1"
    )
    reference_phone_2 = models.CharField(
        max_length=15, blank=True, verbose_name="SĐT Ref 2"
    )
    spouse_phone = models.CharField(
        max_length=15, blank=True, verbose_name="Spouse phone"
    )
    additional_phone_1 = models.CharField(
        max_length=15, blank=True, verbose_name="Add phone 1"
    )
    additional_phone_2 = models.CharField(
        max_length=15, blank=True, verbose_name="Add phone 2"
    )
    assigned_agent = models.CharField(max_length=50, verbose_name="Nhân viên phụ trách")
    contract_number = models.CharField(
        max_length=50, unique=True, verbose_name="Số hợp đồng"
    )
    contract_info = models.TextField(verbose_name="ID Hợp đồng")
    call_source = models.CharField(max_length=100, verbose_name="Nguồn gọi")
    customer_code = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name="fkKH",
    )
    title = models.CharField(max_length=255, blank=True, verbose_name="Tiêu đề")
    id_card_number = models.CharField(
        max_length=20, unique=True, verbose_name="Số CMND"
    )

    customer_name = models.CharField(max_length=255, verbose_name="Tên KH")

    total_overdue = models.IntegerField(
        blank=True, null=False, default=0, verbose_name="Total Overdue"
    )
    tenor = models.CharField(max_length=50, blank=True, verbose_name="Tenor")
    product_group = models.CharField(
        max_length=50, blank=True, verbose_name="PRODUCT_GROUP"
    )
    full_address = models.TextField(blank=True, verbose_name="Địa chỉ đầy đủ")
    district = models.CharField(max_length=100, blank=True, verbose_name="Quận/Huyện")
    city = models.CharField(max_length=100, blank=True, verbose_name="Tỉnh/Thành Phố")
    call_status = models.CharField(
        max_length=50,
        choices=CALL_STATUS_CHOICES,
        blank=True,
        verbose_name="Trạng thái gọi",
    )
    recall_time = models.DateTimeField(blank=True, verbose_name="Thời gian gọi lại")

    call_result = models.CharField(
        max_length=50,
        choices=CALL_RESULT_CHOICES,
        blank=True,
        verbose_name="Kết quả gọi",
    )
    call_reason = models.TextField(blank=True, verbose_name="Lý do gọi")
    scheduled_time = models.DateTimeField(
        blank=True, null=True, verbose_name="Thời gian chỉ định"
    )
    date_final = models.DateTimeField(blank=True, verbose_name="Date final")
    last_action_time = models.DateTimeField(blank=True, verbose_name="Last action time")
    last_action_code = models.CharField(
        max_length=50, blank=True, verbose_name="Last action code"
    )
    last_remark = models.TextField(blank=True, verbose_name="Last remark")
    call_source_uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name="Nguồn",
    )

    def __str__(self):
        return f"{self.contract_number} - {self.customer_name}"
