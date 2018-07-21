from django.urls import path
from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'), #homepage for blogs page
    path('<int:blogId>/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
] 
