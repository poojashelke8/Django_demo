from django.shortcuts import render,get_object_or_404
from .models import Details_Demo

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import generics,status
from .serializers import DetailSerializer,RegisterUser
from .serializers import Detail_Create_Serializer,LoginUser
from rest_framework_simplejwt.tokens import RefreshToken



class DemoViewSet(viewsets.ModelViewSet):
    queryset = Details_Demo.objects.all()
    serializer_class = DetailSerializer

    # CUSTOM ENDPOINTS INSIDE MODELVIEWSET:
    @action(detail=True,methods=['post'])
    def publish(self,request,pk=None):
        demo = self.get_object()
        demo.is_published = True
        demo.save()
        return Response({"status:Published"})
    

class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegisterUser

    def create(self,request,*args,**kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)

        return Response({
            "user": serializer.data,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)
    

@api_view(['POST'])
def LoginApi(request):
    serializer = LoginUser(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response(serializer.validated_data,status=status.HTTP_200_OK)
    
    













    # for different serializers for different use:
    # def get_serializer_class(self):
    # if self.action == 'create':
    #     return DemoCreateSerializer
    # elif self.action == 'update':
    #     return DemoUpdateSerializer
    # elif self.action == 'partial_update':
    #     return DemoUpdateSerializer
    # elif self.action == 'list':
    #     return DemoListSerializer
    # return DemoDetailSerializer

# Create your views here.
# Seperated CRUD fUNCTIONS
# @api_view(['GET'])
# def all_demo(request):
#     demos = Details_Demo.objects.all()
#     serializer = DetailSerializer(demos,many=True)
#     # return render(request,'demo/demo.html',{'demos':demos})
#     return Response(serializer.data)

# @api_view(['GET'])
# def demo_detail(request,pk):
#     demos = get_object_or_404(Details_Demo,pk=pk)
#     serializer = DetailSerializer(demos)
#     # return render(request,'demo/demo.html',{'demos':demos})
#     return Response(serializer.data)

# @api_view(['POST'])
# def demo_create(request):
#     serializer = Detail_Create_Serializer(data = request.data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# @api_view(['PUT','PATCH'])
# def demo_put(request,pk):
#     demo = get_object_or_404(Details_Demo,pk=pk)
#     if request.method == 'PUT':
#         serializer = DetailSerializer(demo,data = request.data)
#     elif request.method == 'PATCH':
#         serializer = DetailSerializer(demo,data=request.data,partial=True)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
    
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)