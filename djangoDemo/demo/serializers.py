from rest_framework import serializers
from .models import Details_Demo

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details_Demo
        fields = '__all__'
