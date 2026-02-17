"""
URL configuration for djangoDemo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from . import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import DemoViewSet,RegisterUserView
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

router = DefaultRouter()
router.register(r'demo_det',DemoViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('api/token/',TokenObtainPairView.as_view()),
    path('register/',RegisterUserView.as_view(),name="register")
]


# urlpatterns = [
#     path('demo_list/',views.all_demo,name="all_demo_detail"),
#     path('demo_list/<int:pk>/',views.demo_detail,name="id_2"),
#     path('demo_create/',views.demo_create,name="demo_create"),
#     path('demo_put/<int:pk>/',views.demo_put,name="demo_put")
# ]

