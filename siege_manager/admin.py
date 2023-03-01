from django.contrib import admin
from .models import Role, Operation, People, Supplies
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Role, Operation, People, Supplies)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('description', 'express_cost')
