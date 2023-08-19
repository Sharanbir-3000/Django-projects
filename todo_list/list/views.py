from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from .models import Task
from list.forms import RegisterForm,TaskForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='loginpage')
def home(request):
    form = Task.objects.filter(name=request.user.username)  
    context = {'form':form}
    return render(request,'home.html',context)

@login_required(login_url='loginpage')
def create_task(request):
    fm = TaskForm()
    if request.method == "POST":
            fm = TaskForm(request.POST)
            if fm.is_valid():
                form = fm.save(commit=False)
                form.name = request.user.username
                form.user = request.user
                form.save()
                return redirect('home')
   
    context = {'form':fm}
    return render(request,'create.html',context)

@login_required(login_url='loginpage')
def view(request,pk):
    task = Task.objects.get(id=pk)
    nm = task.task_name
    form = TaskForm(instance=task)
    context = {'form':form,'nm':nm}
    return render(request,'view.html',context)

@login_required(login_url='loginpage')
def update_task(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form':form}
    return render(request,'update_task.html',context)

@login_required(login_url='loginpage')
def deletion(request,pk):
    form = Task.objects.get(id=pk)
    if request.method == "POST":
        form.delete()
        return redirect('home')

    context = {'form':form}
    return render(request,'delete.html',context)

def register(request):
    fm = RegisterForm()
    if request.method == "POST":
        fm = RegisterForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('loginpage')

    context = {'form':fm}
    return render(request,'register.html',context)

def loginpage(request):
    if request.method == "POST":
        nm = request.POST.get('username')
        ps = request.POST.get('password')
        user = authenticate(request,username=nm,password=ps)
        if user is not None:
            login(request,user)
            return redirect('home')
            
        else:
            return redirect('loginpage')
    context = {}
    return render(request,'loginpage.html',context)

def logout_page(request):
    logout(request)
    return redirect('loginpage')