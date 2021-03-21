from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny

from .models import Bug, Enhancements, Features, Project
from .serializers import (AddUserSerializer, BugSerializers,
                          EnhancementSerializer, FeatureSerializer,
                          ProjectSerializers, UserSerializer)


class BugViewSet(viewsets.ModelViewSet):
    queryset = Bug.objects.all().order_by('name')
    serializer_class = BugSerializers

class ProjectViewset(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('name')
    serializer_class = ProjectSerializers

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer

class FeatureViewset(viewsets.ModelViewSet):
    queryset = Features.objects.all()
    serializer_class = FeatureSerializer

class EnhancementViewset(viewsets.ModelViewSet):
    queryset = Enhancements.objects.all()
    serializer_class = EnhancementSerializer

class AddUserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AddUserSerializer




# class UserCreateAPIView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (AllowAny,)
