from django.shortcuts import render, redirect
from .models import Todo
from pyexpat.errors import messages
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        todo = Todo.objects.filter(user_name=request.user.username)
        if request.method == 'POST':
            new_todo = Todo(
                title=request.POST['title'],
                user_name=request.user.username
                )
            new_todo.save()
            return redirect('/')

        else:    
            return render(request,'index.html', {'todos': todo})
    else:
        return redirect('login')

def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if len(password1) > 7:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username already taken')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password1, first_name=first_name,last_name=last_name)
                    user.save();
                    return redirect('login')
            else:
                messages.info(request, 'Minimum password len = 8')
                return redirect('register')
        else:
            messages.info(request, 'Confirm password not matching')
            return redirect('register')
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')


def status(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.status = not todo.status
    todo.save()
    return redirect('/')

def clearall(request):
    todo = todo = Todo.objects.filter(user_name=request.user.username)
    todo.delete()
    return redirect('/')