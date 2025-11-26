from django.contrib import admin
from django.urls import path, include
from authentication import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),
]