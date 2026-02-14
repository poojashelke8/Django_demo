from django.shortcuts import render,get_object_or_404
from .models import Details_Demo

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import DetailSerializer


# Create your views here.
@api_view(['GET'])
def all_demo(request):
    demos = Details_Demo.objects.all()
    serializer = DetailSerializer(demos,many=True)
    # return render(request,'demo/demo.html',{'demos':demos})
    return Response(serializer.data)

@api_view(['GET'])
def demo_detail(request,pk):
    demos = get_object_or_404(Details_Demo,pk=pk)
    serializer = DetailSerializer(demos)
    # return render(request,'demo/demo.html',{'demos':demos})
    return Response(serializer.data)

@api_view(['POST'])
def demo_create(request):
    serializer = DetailSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    