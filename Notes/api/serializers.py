from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.settings import api_settings

from .models import Bug, Enhancements, Features, Project


class BugSerializers (serializers.ModelSerializer):
    class Meta:
        model = Bug
        fields  = ('__all__')


class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('__all__')

    

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('__all__')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class EnhancementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enhancements
        fields = ('__all__')

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = ('name', 'project',  'description')
        http_method_names = ['post', 'get', 'put', 'patch']

class AddUserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model =User
        fields = ('username', 'password',  'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }
        http_method_names = ['post']

