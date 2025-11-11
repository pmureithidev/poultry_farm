from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('create_flock', views.create_flock, name='create_flock'),
    path('flock_dashboard', views.flock_dashboard, name='flock_dashboard'),
]