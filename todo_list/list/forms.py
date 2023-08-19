from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from list.models import Task

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username",'email','password1','password2']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name','description','status']
        

