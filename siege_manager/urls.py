from . import views
from django.urls import path

urlpatterns = [
    path(
        '',
        views.HomePage.as_view(),
        name='home'
    ),
    path(
        'roles',
        views.RolesView.as_view(),
        name='roles'
    ),
    path(
        'howto',
        views.HowToPage.as_view(),
        name='howto'
    ),
    path(
        'operations',
        views.OperationsPage.as_view(),
        name='operations'
    ),
    path(
        'operationsatk',
        views.OperationsPageAtk.as_view(),
        name='operationsatk'
    ),
    path(
        'moral',
        views.MoralPage.as_view(),
        name='moral'
    ),
    path(
        'supplies',
        views.SuppliesPage.as_view(),
        name='supplies'
    )
]
