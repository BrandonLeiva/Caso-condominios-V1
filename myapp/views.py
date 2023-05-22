from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'myapp/inicio.html')

def AreasAdmin(request):
    return render(request, 'myapp/AreasAdmin.html')