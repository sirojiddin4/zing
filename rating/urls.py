# urls.py

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search_group/', views.search_group, name='search_group'),
    path('credit_table/<int:group_id>/', views.credit_table, name='credit_table'),
    path('edit_credit/<int:student_id>/<int:group_id>/', views.edit_credit, name='edit_credit'),
]
