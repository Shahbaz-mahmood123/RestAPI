import json
import datetime

from django.contrib.auth.models import User
from django.urls import reverse
from .models import Project
from .serializers import ProjectSerializers, AddUserSerializer
from rest_framework import status
from rest_framework.test import APITestCase


class AddUserTestCase(APITestCase):

    def test_adduser(self):
        data = {"username": "testcase", "password": "exteremlystrongpassword!0", "email":"testemail@test.com",
         "first_name":"test_first_name","last_name":"test_last_name" }
        response = self.client.post("/adduser/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    

class ProjectTestCase(APITestCase):

    def test_post_project(self):
        data = { "name": "testcase", "description": "Long Description for test case!0", "created_by": 1}
        response= self.client.post("/projects/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_project(self):
        response = self.client.get("/projects/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class BugsTestCase(APITestCase):
    
    def test_post_bugs(self):
        data = {
        "id": 1,"name": "test", "description": "test", "subject": "test", "steps_to_reproduce": "test", "bug_priority": "P2", 
        "project": 1, "created_date": "2021-03-14T16:59:00Z", "created_by": 1 }
        response= self.client.post("/bugs/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        

    def test_get_bugs(self):
        response= self.client.get("/bugs/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class JWTTestCase(APITestCase):

    def setUp(self):
        self.username = 'JohnSmith19'
        self.password = 'jieowjfrewofjewfj'
        self.data = {
            'username': self.username,
            'password': self.password
        }

    def test_current_user(self):

        user = User.objects.create_user(username='JohnSmith19', email='JohnSmith19@smith.com', password='jieowjfrewofjewfj')
        self.assertEqual(user.is_active, 1, 'Active User')

        response = self.client.post("/api/token/", self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)

class FeatureTestCase(APITestCase):

        
    def test_Feature(self):

        user = User.objects.create_user(username='JohnSmith19', email='JohnSmith19@smith.com', password='jieowjfrewofjewfj')
        self.assertEqual(user.is_active, 1, 'Active User')

        project = Project.objects.create("name")

        data = {
        "name": "test", "description": "test", "project":1 }
        response= self.client.post("/bugs/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
