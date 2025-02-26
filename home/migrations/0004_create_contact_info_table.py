# Generated by Django 4.2.17 on 2025-02-24 06:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0003_initial"),
    ]

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
    ]
