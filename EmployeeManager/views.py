from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Home.html' )
def view(request):
    return render(request, 'View_Employee.html' )