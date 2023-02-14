from django.urls import path, include
from . import views

urlpatterns = [

path('home', views.index, name='index'),
path('view', views.view, name='view'),
path('add_emp', views.add_emp, name='add_emp'),
path('all_emp', views.all_emp, name='all_emp'),
path('filter_emp', views.filter_emp, name='filter_emp'),
]
