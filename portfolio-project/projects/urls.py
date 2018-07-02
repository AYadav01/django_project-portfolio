from django.urls import path
from . import views

urlpatterns = [
    path('', views.allprojects, name='allprojects'), #homepage for blogs page
    path('1/', views.wordcounter, name='wordcounter'),
    path('1/a', views.count, name='count'),
    path('2/', views.htmlTag, name='htmlTag'),
    path('2/a', views.htmlTagFinder, name='htmlTagFinder'),
] 
