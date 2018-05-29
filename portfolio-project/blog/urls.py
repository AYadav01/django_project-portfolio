from django.urls import path
from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'), #homepage for blogs page
    path('<int:blog_id>/', views.detail, name='detail'),
] 
