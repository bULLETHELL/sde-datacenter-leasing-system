from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import NewUserForm

# Create your views here.
def homepage(request):
    return render(request=request,
                  template_name='main/home.html')

def profile(request):
    return render(request=request,
                  template_name='main/profile.html')

def lease(request):
    return render(request=request,
                  template_name='main/lease.html')

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')

    form = AuthenticationForm()
    return render(request=request,
                  template_name = 'main/home.html',
                  context={'form':form})

def logout_request(request):
    logout(request)
    return redirect('main:homepage')

def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect('main:homepage')
        
        else:
            return render(request=request,
                  template_name = 'main/register.html',
                  context={'form':form})

    form = NewUserForm              
    return render(request=request,
                  template_name = 'main/register.html',
                  context={'form':form})
