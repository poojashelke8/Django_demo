from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Just show up")
    return render(request,'websites/index.html')

def fun(request):
    return HttpResponse("I am enjoying the Django")
