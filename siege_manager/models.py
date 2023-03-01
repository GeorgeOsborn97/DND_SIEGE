from django.db import models

# Create your models here.


class Supplies(models.Model):
    supply = models.CharField(max_length=200, unique=True, primary_key=True)
    description = models.TextField(blank=True)


class People(models.Model):
    occupation = models.CharField(max_length=200, unique=True, primary_key=True)
    description = models.TextField(blank=True)


class Operation(models.Model):
    title = models.CharField(max_length=50, primary_key=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    resources_required = models.ManyToManyField(Supplies, related_name='resources_req')
    people_required = models.ManyToManyField(People, related_name='people_req')
    express_cost = models.TextField(blank=True)


class Role(models.Model):
    title = models.CharField(max_length=50, primary_key=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    operation_options = models.ManyToManyField(Operation, related_name='ops')
