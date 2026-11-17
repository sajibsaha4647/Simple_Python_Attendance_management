from django.urls import path

from . import controllers

app_name = 'employee'

urlpatterns = [
    path('create/', controllers.create_employee, name='create'),
]
