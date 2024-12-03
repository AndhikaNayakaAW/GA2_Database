# yellow/urls.py

from django.urls import path
from . import views

app_name = 'yellow'

urlpatterns = [
    path('iflogin/', views.iflogin_view, name='iflogin'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('role_selection/', views.role_selection_view, name='role_selection'), 
    path('user_register/', views.user_register_view, name='user_register'),  
    path('worker_register/', views.worker_register_view, name='worker_register'), 
    path('worker_register/', views.worker_register_view, name='worker_register'), 
]