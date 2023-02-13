from django.shortcuts import render, HttpResponse
from . models import Employee

def view_emp(request, emp_id=0):
    try:
        emp = Employee.objects.get(id = emp_id)
        context = {'emp': emp}
        return HttpResponse(context)
    except:
        return HttpResponse('Error occured')    
        
        

# Create your views here.
