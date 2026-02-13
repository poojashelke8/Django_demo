from django.shortcuts import render
from .models import Details_Demo

# Create your views here.
def all_demo(request):
    demos = Details_Demo.objects.all()
    return render(request,'demo/demo.html',{'demos':demos})