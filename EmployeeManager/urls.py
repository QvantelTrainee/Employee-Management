from django.urls import path, include
from . import views

urlpatterns = [
   path('view_emp/<int:emp_id>', views.view_emp)
]