# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# from .forms import *
# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE,blank=True)
    
    name = models.CharField(max_length=200,null=True)
    
    task_name = models.CharField(max_length=20,null=True,default="")
    description = models.TextField(max_length=300,null=True,blank=True)
    status = models.BooleanField(default=False)
    date_task = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.task_name
