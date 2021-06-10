from django.http.response import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html',{'name':'sameer'})
def add(request):
    val1=int(request.GET['num1'])
    val2=int(request.GET['num2'])
    result = val1+val2
    return render(request,'result.html',{'result':result})
