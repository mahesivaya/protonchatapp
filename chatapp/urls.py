from django.urls import path, include
from . import views

app_name = 'chatapp'


urlpatterns = [
    path('', views.index, name='index'),
]
