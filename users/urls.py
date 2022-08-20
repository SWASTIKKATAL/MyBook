
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('createuser/',views.create_user),
    path('allusers/',views.getall_users),
    path('allusers/<id>/',views.login_user)
]