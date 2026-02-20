from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Details_Demo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details_Demo
        fields = '__all__'

class Detail_Create_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Details_Demo
        fields = ['name', 'description', 'type']

class RegisterUser(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ['username','password']
        extra_kwargs = {
            'username':{
                'error_messages':{
                    'unique':'This username is alreday taken,try different!!'
                }
            }
        }

    def create(self,validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            password = validated_data['password']
        )
        return user
class LoginUser(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)
    
    def validate(self,data):
        user = authenticate(
            username = data['username'],
            password =data['password']
        )

        if not user:
            raise serializers.ValidationError("Invalid username and password")
        
        refresh = RefreshToken.for_user(user)
        return {
            "username":user.username,
            "refresh":str(refresh),
            "access":str(refresh.access_token)
        }