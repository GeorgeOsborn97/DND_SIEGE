# Generated by Django 3.2.18 on 2023-03-08 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siege_manager', '0009_operation_attack_or_defend'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operation',
            old_name='Attack_or_defend',
            new_name='attack_or_defend',
        ),
    ]
