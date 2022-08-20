
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('create/',views.create_notes),
    path('allnotes/',views.getall_notes),
    path('detailedview/<id>/',views.detail_view)
]