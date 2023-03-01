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
    )
]
