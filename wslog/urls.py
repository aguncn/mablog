# coding:utf8
from django.urls import path
from .views import log_add, log_show


urlpatterns = [

    path('log_show/', log_show, name="log_show"),
    path('log_add/', log_add, name="log_add"),
]