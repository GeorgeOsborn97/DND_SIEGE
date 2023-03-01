# Generated by Django 3.2.18 on 2023-03-01 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('title', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True)),
                ('express_cost', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('occupation', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supplies',
            fields=[
                ('supply', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('title', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True)),
                ('operation_options', models.ManyToManyField(related_name='ops', to='siege_manager.Operation')),
            ],
        ),
        migrations.AddField(
            model_name='operation',
            name='people_required',
            field=models.ManyToManyField(related_name='people_req', to='siege_manager.People'),
        ),
        migrations.AddField(
            model_name='operation',
            name='resources_required',
            field=models.ManyToManyField(related_name='resources_req', to='siege_manager.Supplies'),
        ),
    ]