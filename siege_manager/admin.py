from django.contrib import admin
from .models import Role, Operation, People, Supplies
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Role, Operation)
class RoleOps(SummernoteModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description', 'express_cost')


@admin.register(People, Supplies)
class PeopleSuppliesAdmin(SummernoteModelAdmin):
    summernote_fields = ('description')
