from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .form import RegisterUser
from django.contrib.auth.decorators import login_required


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("There was error logging into this Account"))
            return redirect("login")
    
    else:
        return render(request, 'auths/login.html', {})
    
def register_user(request):
    if request.method =="POST":
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,("Registration Successful"))
            return redirect('home')
    else:
        form = RegisterUser()
    return render(request, 'auths/registration.html', {'form':form})

def logout_user(request):
    logout(request)
    messages.success(request, ("You Are Logout, Try Login Again"))
    return redirect('home')
