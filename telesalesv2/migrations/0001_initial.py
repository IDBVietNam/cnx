# Generated by Django 4.2.18 on 2025-03-03 01:15

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TelesalesV2",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_modified", models.DateTimeField(auto_now=True)),
                (
                    "mobile_number",
                    models.CharField(blank=True, max_length=15, verbose_name="Di động"),
                ),
                (
                    "reference_phone_1",
                    models.CharField(
                        blank=True, max_length=15, verbose_name="SĐT Ref 1"
                    ),
                ),
                (
                    "reference_phone_2",
                    models.CharField(
                        blank=True, max_length=15, verbose_name="SĐT Ref 2"
                    ),
                ),
                (
                    "spouse_phone",
                    models.CharField(
                        blank=True, max_length=15, verbose_name="Spouse phone"
                    ),
                ),
                (
                    "additional_phone_1",
                    models.CharField(
                        blank=True, max_length=15, verbose_name="Add phone 1"
                    ),
                ),
                (
                    "additional_phone_2",
                    models.CharField(
                        blank=True, max_length=15, verbose_name="Add phone 2"
                    ),
                ),
                (
                    "assigned_agent",
                    models.CharField(max_length=50, verbose_name="Nhân viên phụ trách"),
                ),
                (
                    "contract_number",
                    models.CharField(
                        max_length=50, unique=True, verbose_name="Số hợp đồng"
                    ),
                ),
                ("contract_info", models.TextField(verbose_name="ID Hợp đồng")),
                (
                    "call_source",
                    models.CharField(max_length=100, verbose_name="Nguồn gọi"),
                ),
                (
                    "customer_code",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        unique=True,
                        verbose_name="fkKH",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Tiêu đề"
                    ),
                ),
                (
                    "id_card_number",
                    models.CharField(
                        max_length=20, unique=True, verbose_name="Số CMND"
                    ),
                ),
                (
                    "customer_name",
                    models.CharField(max_length=255, verbose_name="Tên KH"),
                ),
                (
                    "total_overdue",
                    models.IntegerField(
                        blank=True, default=0, verbose_name="Total Overdue"
                    ),
                ),
                (
                    "tenor",
                    models.CharField(blank=True, max_length=50, verbose_name="Tenor"),
                ),
                (
                    "product_group",
                    models.CharField(
                        blank=True, max_length=50, verbose_name="PRODUCT_GROUP"
                    ),
                ),
                (
                    "full_address",
                    models.TextField(blank=True, verbose_name="Địa chỉ đầy đủ"),
                ),
                (
                    "district",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Quận/Huyện"
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Tỉnh/Thành Phố"
                    ),
                ),
                (
                    "call_status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("new", "New"),
                            ("follow1", "Follow1"),
                            ("follow2", "Follow2"),
                            ("follow3", "Follow3"),
                        ],
                        max_length=50,
                        verbose_name="Trạng thái gọi",
                    ),
                ),
                (
                    "recall_time",
                    models.DateTimeField(blank=True, verbose_name="Thời gian gọi lại"),
                ),
                (
                    "call_result",
                    models.CharField(
                        blank=True,
                        choices=[
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
                        ],
                        max_length=50,
                        verbose_name="Kết quả gọi",
                    ),
                ),
                ("call_reason", models.TextField(blank=True, verbose_name="Lý do gọi")),
                (
                    "scheduled_time",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Thời gian chỉ định"
                    ),
                ),
                (
                    "date_final",
                    models.DateTimeField(blank=True, verbose_name="Date final"),
                ),
                (
                    "last_action_time",
                    models.DateTimeField(blank=True, verbose_name="Last action time"),
                ),
                (
                    "last_action_code",
                    models.CharField(
                        blank=True, max_length=50, verbose_name="Last action code"
                    ),
                ),
                (
                    "last_remark",
                    models.TextField(blank=True, verbose_name="Last remark"),
                ),
                (
                    "call_source_uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        unique=True,
                        verbose_name="Nguồn",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
