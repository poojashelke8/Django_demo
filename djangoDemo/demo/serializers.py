from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Details_Demo,User

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details_Demo
        fields = '__all__'

class Detail_Create_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Details_Demo
        fields = ['name', 'description', 'type']

class RegisterUser(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True),

    class Meta:
        model = User
        fields = ['username','password']

        def create(self,validated_data):
            user = User.objects.create_user(
                username = validated_data['username'],
                password = validated_data['password']
            )
            return user