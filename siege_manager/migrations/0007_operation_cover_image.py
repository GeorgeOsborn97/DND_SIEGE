# Generated by Django 3.2.18 on 2023-03-07 14:32

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siege_manager', '0006_operation_operation_benefit'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='cover_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]