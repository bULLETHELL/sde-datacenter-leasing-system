from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import NewUserForm, LoginForm, LeaseForm
from .models import InventoryItem, InventoryItemType, Loan, User
from datetime import date


# Create your views here.
def homepage(request):
    return render(request=request,
                  template_name='main/home.html',
                  context={'loginForm': LoginForm})


def profile(request):
    return render(request=request,
                  template_name='main/profile.html',
                  context={'loginForm': LoginForm})


def lease(request):
    return render(request=request,
                  template_name='main/lease.html',
                  context={'loginForm':LoginForm, 'inventoryItems':InventoryItem.objects.all, 'inventoryItemTypes':InventoryItemType.objects.all, 'loans':Loan.objects.all})

def lease_request(request):
    if request.method == 'POST':
        leaseForm = LeaseForm(request.POST)
        if leaseForm.is_valid():
            itemName = leaseForm.cleaned_data.get('itemName')
            itemDescription = leaseForm.cleaned_data.get('itemDescription')
            itemSoftware = leaseForm.cleaned_data.get('itemSoftware')
            itemType = leaseForm.cleaned_data.get('itemType')
            itemOS = leaseForm.cleaned_data.get('itemOS')
            itemAvailable = leaseForm.cleaned_data.get('itemAvailable')

            newLoan = Loan(loanedItem = model, loanStartDate = )

def login_request(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')

    form = LoginForm
    return render(request=request,
                  template_name='main/header.html',
                  context={'form': form})


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
                          template_name='main/register.html',
                          context={'form': form, 'loginForm': LoginForm})

    form = NewUserForm
    return render(request=request,
                  template_name='main/register.html',
                  context={'form': form, 'loginForm': LoginForm})
