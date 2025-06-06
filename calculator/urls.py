from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('set/', views.set, name='set'),
]