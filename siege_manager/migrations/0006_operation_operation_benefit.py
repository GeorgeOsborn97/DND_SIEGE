# Generated by Django 3.2.18 on 2023-03-07 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siege_manager', '0005_operation_days_required'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='operation_benefit',
            field=models.TextField(default='to be added'),
        ),
    ]