from rest_framework import serializers
from .models import Company , userModel

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'

class userSerializer(serializers.ModelSerializer):

    class Meta:
        model = userModel
        fields = '__all__'