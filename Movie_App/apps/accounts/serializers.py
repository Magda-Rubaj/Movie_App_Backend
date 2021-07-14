from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}, 'email': {'required': True}}
    
    def create(self, validated_data):
        ModelClass = self.Meta.model
        instance = ModelClass.objects.create(**validated_data)   
        if instance.password is not None:
            instance.set_password(instance.password)           
        instance.save()
        return instance

class EmailTokenSerializer(TokenObtainPairSerializer):
    username_field = get_user_model().EMAIL_FIELD