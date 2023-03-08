from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Role, Operation, People, Supplies

# Create your views here.


class HomePage(View):
    def get(self, request):
        return render(request, '../templates/index.html')


class HowToPage(View):
    def get(self, request):
        return render(request, '../templates/howto.html')


class OperationsPage(View):
    def get(self, request):
        operation_list = Operation.objects.all()

        context = {
            'operation_list': operation_list,
        }
        return render(request, '../templates/operations.html', context)


class OperationsPageAtk(View):
    def get(self, request):
        operation_list = Operation.objects.all()

        context = {
            'operation_list': operation_list,
        }
        return render(request, '../templates/operationsatk.html', context)


class SuppliesPage(View):
    def get(self, request):
        supply_list = Supplies.objects.all()
        unit_list = People.objects.all()

        context = {
            'supply_list': supply_list,
            'unit_list': unit_list
        }
        return render(request, '../templates/supplies.html', context)


class MoralPage(View):
    def get(self, request):
        return render(request, '../templates/moral.html')


class RolesView(View):
    def get(self, request, *args, **kwargs):
        role_list = Role.objects.all()

        context = {
            'role_list': role_list,
        }
        return render(request, '../templates/roles.html', context)