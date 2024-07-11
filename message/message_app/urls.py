from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create',views.create),        
    path('',views.dashboard),
    path('delete/<rid>',views.delete),
    path('edit/<rid>',views.edit)
   
]
