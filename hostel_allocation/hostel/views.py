from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserLoginForm
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib import messages



def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    context = {}
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request,user)
            
            
            return redirect('index')
        else:
            redirect('register')
            form = UserLoginForm()
            context['form'] = form
    else:
        form = UserLoginForm()
        context['form'] = form
    return render(request,'login.html', context)

def register_view(request):
    context = {}
    # if request.user.is_authenticated:
    #     return redirect('loginpage')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            #password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=password)
            #login(request,user)
            return redirect('loginpage')
        else:
            form = UserCreationForm()
            context['form'] = form
            return redirect('register')
    else:
        form = UserCreationForm()
        context['form'] = form
    return render(request,'register.html', context)
    



@login_required(login_url = '/user_login/')
def dashboard (request):
    return render(request,'root/index.html',{})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("loginpage")


def home_view(request):
    return render(request, 'index.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')