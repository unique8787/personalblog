from django.urls import path

from blog import admin
from . import views

urlpatterns = [
    path('', views.bloghome, name='bloghome'),
    path('<str:slug>/', views.blogpost, name='blogpost')
  
]