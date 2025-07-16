from django.shortcuts import render
from  django.http import HttpResponse
def my_view(request):
    return render(request,'hellow.html',{'name':'python is free'})
# Create your views here.
def add(request):
    val1 = request.POST['number1']
    val2 = request.POST['number2']
    val3= int(val1) + int(val2)
    return render(request,'result.html',{'result':val3})