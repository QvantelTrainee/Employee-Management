from django.urls import path, include
from . import views

urlpatterns = [
   path('add_emp', views.add_emp, name='add_emp'),
    
   ]