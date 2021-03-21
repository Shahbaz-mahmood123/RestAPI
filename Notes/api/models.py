import datetime

from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(max_length=1000)
    created_date= models.DateTimeField(default = datetime.datetime.now())
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
   


    def __str__(self):
        return self.name

class Bug(models.Model):
    name = models.CharField(max_length=60)
    subject = models.CharField(max_length=60)
    description = models.TextField(max_length=1000)
    steps_to_reproduce = models.TextField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date= models.DateTimeField(default = datetime.datetime.now())
    due_date = models.DateTimeField(default = datetime.datetime.now())


    P4 ='P4'
    P3 ='P3'
    P2 ='P2'
    P1 ='P1'
    priority = [
        (P4 ,'Low'),
        (P3 , 'Medium'),
        (P2, 'High'),
        (P1, 'Critical'),
    ]
    bug_priority = models.CharField(
        max_length=2,
        choices = priority,
        default = P4,
    )

    def __str__(self):
        return self.name
        

class Enhancements (models.Model):
    name = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date= models.DateTimeField(default = datetime.datetime.now())
    description = models.TextField(max_length=1000)
    due_date = models.DateTimeField(default = datetime.datetime.now())
    
    def __str__(self):
        return self.name

class Features(models.Model):
    name = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date= models.DateTimeField(default = datetime.datetime.now())
    description = models.TextField(max_length=1000)
    due_date = models.DateTimeField(default = datetime.datetime.now())
    assigned_to =models.ManyToManyField(User,related_name='assigned_to', blank=True)

    P4 ='P4'
    P3 ='P3'
    P2 ='P2'
    P1 ='P1'
    priority = [
        (P4 ,'Low'),
        (P3 , 'Medium'),
        (P2, 'High'),
        (P1, 'Critical'),
    ]
    priority = models.CharField(
        max_length=2,
        choices = priority,
        default = P4,
    )

    def __str__(self):
        return self.name





    

    
