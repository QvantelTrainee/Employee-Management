from django.urls import path, include
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.index, name='index'),
]
=======
   path('add_emp', views.add_emp, name='add_emp'),
   path('all_emp', views.all_emp, name='all_emp'),
   path('filter_emp', views.filter_emp, name='filter_emp'),
   ]
>>>>>>> 92feefcd5c21bf69d0c64030aa8f9bc8a0be4e50
