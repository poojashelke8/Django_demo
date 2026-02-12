from django.shortcuts import render

# Create your views here.
def all_demo(request):
    return render(request,'demo/demo.html')