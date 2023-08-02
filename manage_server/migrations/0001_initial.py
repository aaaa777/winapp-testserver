# Generated by Django 4.2.3 on 2023-08-02 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ManagedPC",
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
                ("hostname", models.CharField(help_text="PC hostname", max_length=100)),
                (
                    "device_id",
                    models.CharField(help_text="PC device ID", max_length=100),
                ),
                (
                    "management_id",
                    models.CharField(
                        help_text='PC management ID like "PXXX-XXX"', max_length=100
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="last update"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ManagedPCUser",
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
                ("user_id", models.CharField(help_text="User ID", max_length=100)),
                (
                    "user_displayname",
                    models.CharField(help_text="User name", max_length=100),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="last update"),
                ),
                (
                    "managed_pc",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="manage_server.managedpc",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OperationLog",
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
                ("operation", models.CharField(help_text="Operation", max_length=100)),
                (
                    "operation_status",
                    models.CharField(help_text="Operation status", max_length=100),
                ),
                (
                    "operation_result",
                    models.CharField(help_text="Operation result", max_length=100),
                ),
                ("operation_time", models.DateTimeField(verbose_name="operation time")),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="last update"),
                ),
                (
                    "managed_pc",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="manage_server.managedpc",
                    ),
                ),
                (
                    "managed_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="manage_server.managedpcuser",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AccessToken",
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
                (
                    "access_token",
                    models.CharField(help_text="Access token", max_length=100),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now=True, verbose_name="last update"),
                ),
                (
                    "expires_in",
                    models.IntegerField(default=0, help_text="Expires in seconds"),
                ),
                (
                    "managed_user",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="manage_server.managedpcuser",
                    ),
                ),
            ],
        ),
    ]
