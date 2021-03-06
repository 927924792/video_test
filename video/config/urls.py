# coding:utf-8

from django.contrib import admin
from django.urls import path, include
from app.client import urls as client_urls
from app.dashboard import urls as dashboard_urls

urlpatterns = [
    path('client', include(client_urls)),
    path('dashboard', include(dashboard_urls))
]
