import uuid

from django.db import models


class TelesalesV2(models.Model):
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
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Ngày tạo"
    )  # DateCreated
    mobile_number = models.CharField(
        max_length=15, blank=True, verbose_name="Di động"
    )  # Di động
    reference_phone_1 = models.CharField(
        max_length=15, blank=True, verbose_name="SĐT Ref 1"
    )  # SDT Ref 1
    reference_phone_2 = models.CharField(
        max_length=15, blank=True, verbose_name="SĐT Ref 2"
    )  # SDT Ref 2
    spouse_phone = models.CharField(
        max_length=15, blank=True, verbose_name="Spouse phone"
    )  # Spousephone
    additional_phone_1 = models.CharField(
        max_length=15, blank=True, verbose_name="Add phone 1"
    )  # Add phone 1
    additional_phone_2 = models.CharField(
        max_length=15, blank=True, verbose_name="Add phone 2"
    )  # Add phone 2
    assigned_agent = models.CharField(
        max_length=50, verbose_name="Nhân viên phụ trách"
    )  # Nhân viên phụ trách
    contract_number = models.CharField(
        max_length=50, unique=True, verbose_name="Số hợp đồng"
    )  # Số hợp đồng
    # ID Hợp đồng (Chứa thông tin SHD, KH, CCCD, Nợ,...)
    contract_info = models.TextField(verbose_name="ID Hợp đồng")
    call_source = models.CharField(
        max_length=100, verbose_name="Nguồn gọi"
    )  # Nguồn gọi
    customer_code = models.UUIDField(
        # UUID thay thế c_fkKH
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name="fkKH",
    )
    title = models.CharField(
        max_length=255, blank=True, verbose_name="Tiêu đề"
    )  # Tiêu đề
    id_card_number = models.CharField(
        max_length=20, unique=True, verbose_name="Số CMND"
    )  # Số CMND (CCCD)

    customer_name = models.CharField(max_length=255, verbose_name="Tên KH")  # Tên KH

    total_overdue = models.IntegerField(
        blank=True, null=False, default=0, verbose_name="Total Overdue"
    )
    tenor = models.CharField(max_length=50, blank=True, verbose_name="Tenor")  # Tenor
    product_group = models.CharField(
        max_length=50, blank=True, verbose_name="PRODUCT_GROUP"
    )  # PRODUCT_GROUP
    full_address = models.TextField(
        blank=True, verbose_name="Địa chỉ đầy đủ"
    )  # Địa chỉ đầy đủ
    district = models.CharField(
        max_length=100, blank=True, verbose_name="Quận/Huyện"
    )  # Quận/Huyện
    city = models.CharField(
        max_length=100, blank=True, verbose_name="Tỉnh/Thành Phố"
    )  # Tỉnh/Thành Phố
    call_status = models.CharField(
        max_length=50,
        choices=CALL_STATUS_CHOICES,
        blank=True,
        verbose_name="Trạng thái gọi",
    )
    recall_time = models.DateTimeField(
        blank=True, verbose_name="Thời gian gọi lại"
    )  # Thời gian gọi lại

    call_result = models.CharField(
        max_length=50,
        choices=CALL_RESULT_CHOICES,
        blank=True,
        verbose_name="Kết quả gọi",
    )
    call_reason = models.TextField(blank=True, verbose_name="Lý do gọi")  # Lý do gọi
    scheduled_time = models.DateTimeField(
        blank=True, null=True, verbose_name="Thời gian chỉ định"
    )  # Thời gian chỉ định
    date_final = models.DateTimeField(
        blank=True, verbose_name="Date final"
    )  # Date final
    last_action_time = models.DateTimeField(
        blank=True, verbose_name="Last action time"
    )  # Last action time
    last_action_code = models.CharField(
        max_length=50, blank=True, verbose_name="Last action code"
    )  # Last action code
    last_remark = models.TextField(
        blank=True, verbose_name="Last remark"
    )  # Last remark
    call_source_uuid = models.UUIDField(
        # c_nguon (UUID)
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name="Nguồn",
    )

    def __str__(self):
        return f"{self.contract_number} - {self.customer_name}"
