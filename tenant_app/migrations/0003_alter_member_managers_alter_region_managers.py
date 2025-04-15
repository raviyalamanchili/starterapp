# Generated by Django 4.2.20 on 2025-04-15 22:43

from django.db import migrations
import django_multitenant.models


class Migration(migrations.Migration):

    dependencies = [
        ('tenant_app', '0002_alter_member_managers_alter_region_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='member',
            managers=[
                ('objects', django_multitenant.models.TenantManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='region',
            managers=[
                ('objects', django_multitenant.models.TenantManager()),
            ],
        ),
    ]
