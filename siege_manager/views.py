from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Role, Operation, People, Supplies

# Create your views here.


class HomePage(View):
    def get(self, request):
        return render(request, '../templates/index.html')


class RolesView(View):
    def get(self, request, *args, **kwargs):
        role_list = Role.objects.all()

        context = {
            'role_list': role_list,
        }
        return render(request, '../templates/roles.html', context)