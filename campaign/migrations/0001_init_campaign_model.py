# Generated by Django 4.2.17 on 2025-02-24 09:10

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ContactInfo",
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
                    "penalty_amount",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "interest_amount",
                    models.DecimalField(decimal_places=2, max_digits=12),
                ),
                (
                    "principal_amount",
                    models.DecimalField(decimal_places=2, max_digits=12),
                ),
                ("pos_assign", models.DecimalField(decimal_places=2, max_digits=12)),
                ("last_result_final", models.CharField(max_length=100)),
                ("total_amount", models.DecimalField(decimal_places=2, max_digits=12)),
                ("date_start", models.DateField()),
                ("date_end", models.DateField()),
                ("total_payment", models.DecimalField(decimal_places=2, max_digits=12)),
                ("assign_invalid_date", models.DateField()),
                ("payment_request_date", models.DateField()),
                ("obs_due_no", models.IntegerField()),
                ("loan_term", models.IntegerField()),
                ("loan_amount", models.DecimalField(decimal_places=2, max_digits=12)),
                ("mob", models.IntegerField()),
                ("dpd_assign", models.IntegerField()),
                ("dpd_current", models.IntegerField()),
                ("current_account", models.CharField(max_length=100)),
                ("contract_date", models.DateField()),
                ("contract_number", models.CharField(max_length=100)),
                ("loan_id", models.CharField(max_length=100)),
                ("late_days", models.IntegerField(default=0)),
                ("monthly_payment", models.IntegerField(default=0)),
            ],
            options={
                "db_table": "contact_info",
            },
        ),
        migrations.CreateModel(
            name="CustomerInfo",
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
                ("name", models.CharField(max_length=255)),
                ("gender", models.CharField(max_length=50)),
                ("id_number", models.CharField(max_length=20, unique=True)),
                ("day_of_birth", models.DateField()),
                (
                    "family_relation",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("agency", models.CharField(blank=True, max_length=255, null=True)),
                ("contract_number", models.CharField(max_length=100)),
                (
                    "company_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "company_address",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "company_district",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "company_province",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("group", models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                "db_table": "customer_info",
            },
        ),
        migrations.CreateModel(
            name="PaymentInfo",
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
                ("first_paid_date", models.DateField()),
                ("account_number", models.CharField(max_length=100)),
                (
                    "largest_amount",
                    models.DecimalField(decimal_places=2, max_digits=12),
                ),
                ("last_payment_date", models.DateField()),
                ("disbursement_date", models.DateField()),
                ("cif", models.CharField(max_length=100)),
                ("due_date_overdue", models.DateField()),
                ("next_due_date", models.DateField()),
                (
                    "next_due_amount",
                    models.DecimalField(decimal_places=2, max_digits=12),
                ),
                (
                    "future_prin_amt",
                    models.DecimalField(decimal_places=2, max_digits=12),
                ),
                ("remain_prin", models.DecimalField(decimal_places=2, max_digits=12)),
                ("pos_bom", models.DecimalField(decimal_places=2, max_digits=12)),
            ],
            options={
                "db_table": "payment_info",
            },
        ),
    ]
