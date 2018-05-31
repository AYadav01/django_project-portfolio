from django.urls import path
from . import views

urlpatterns = [
    path('', views.allprojects, name='allprojects'), #homepage for blogs page

] 
