from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import NewUserForm, LoginForm, LeaseForm
from .models import InventoryItem, InventoryItemType, Loan, User, Reservation
from datetime import date


# Create your views here.
def homepage(request):
    return render(request=request,
                  template_name='main/home.html',
                  context={'loginForm': LoginForm, 'username': request.user.username})


def profile(request, username):
    username = request.user.username
    return render(request=request,
                  template_name='main/profile.html',
                  context={'loginForm': LoginForm, 'username': username})


def profile_settings(request, username):
    username = request.user.username
    return render(request=request,
                  template_name='main/profile/settings.html',
                  context={'loginForm': LoginForm, 'username': username})


def lease(request):
    today = date.today()
    todayFormatted = today.strftime("%d/%m/%Y")
    # todayList = todayFormatted.split('/')
    # todayFormattedCorrectly = f"{todayList[0]}-{todayList[1]}-{todayList[2]}"
    return render(request=request,
                  template_name='main/lease.html',
                  context={'loginForm': LoginForm, 'inventoryItems': InventoryItem.objects.all,
                           'inventoryItemTypes': InventoryItemType.objects.all, 'loans': Loan.objects.all,
                           'leaseForm': LeaseForm, 'datetoday': todayFormatted, 'user': request.user})


def returnLoan(request):
    today = date.today()
    todayFormatted = today.strftime("%d/%m/%Y")
    return render(request=request,
                  template_name='main/return.html',
                  context={'loginForm': LoginForm, 'inventoryItems': InventoryItem.objects.all,
                           'inventoryItemTypes': InventoryItemType.objects.all, 'loans': Loan.objects.all,
                           'leaseForm': LeaseForm, 'datetoday': todayFormatted, 'user': request.user})


def reserve(request):
    today = date.today()
    todayFormatted = today.strftime("%d/%m/%Y")
    # todayList = todayFormatted.split('/')
    # todayFormattedCorrectly = f"{todayList[0]}-{todayList[1]}-{todayList[2]}"
    return render(request=request,
                  template_name='main/reservation.html',
                  context={'loginForm': LoginForm, 'inventoryItems': InventoryItem.objects.all,
                           'inventoryItemTypes': InventoryItemType.objects.all, 'loans': Loan.objects.all,
                           'leaseForm': LeaseForm, 'datetoday': todayFormatted, 'user': request.user})


def reserve_request(request):
    if request.method == 'POST':
        itemId = request.POST.get("itemID")
        reservedItem = InventoryItem.objects.get(pk=itemId)
        reservationStartDate = request.POST.get("reservationStartDate")
        reservationEndDate = request.POST.get("reservationEndDate")
        reservingUser = request.POST.get("reservingUser")
        reservedFor = request.POST.get('reservedFor')
        reservationPurpose = request.POST.get("reservationPurpose")

        startDateSplit = reservationStartDate.split('/')
        endDateSplit = reservationEndDate.split('/')
        startDateFixed = f"{startDateSplit[2]}-{startDateSplit[1]}-{startDateSplit[0]}"
        endDateFixed = f"{endDateSplit[2]}-{endDateSplit[1]}-{endDateSplit[0]}"

        newReservation = Reservation(reservedItem=reservedItem, reservingUser=User.objects.get(username=reservingUser),
                                     reservationStartDate=startDateFixed, reservationEndDate=endDateFixed,
                                     reservedFor=User.objects.get(username=reservedFor),
                                     reservationPurpose=reservationPurpose)
        newReservation.save()
        print(itemId, reservedItem, reservationStartDate, reservationEndDate, reservingUser, reservedFor,
              reservationPurpose)
        return redirect("main:reserve")


def lease_request(request):
    if request.method == 'POST':
        itemId = request.POST.get("itemID")
        loanedItem = InventoryItem.objects.get(pk=itemId)
        loanStartDate = request.POST.get("loanStartDate")
        loanEndDate = request.POST.get("loanEndDate")
        loaningUser = request.POST.get("loaningUser")
        loanPurpose = request.POST.get("loanPurpose")

        startDateSplit = loanStartDate.split('/')
        endDateSplit = loanEndDate.split('/')
        startDateFixed = f"{startDateSplit[2]}-{startDateSplit[1]}-{startDateSplit[0]}"
        endDateFixed = f"{endDateSplit[2]}-{endDateSplit[1]}-{endDateSplit[0]}"

        newLoan = Loan(loanedItem=loanedItem, loanStartDate=startDateFixed, loanEndDate=endDateFixed,
                       loaningUser=User.objects.get(username=loaningUser), loanPurpose=loanPurpose)
        newLoan.save()
        loanedItem.itemAvailable = False
        loanedItem.save()
        print(loanedItem, loanStartDate, loanEndDate, loaningUser, loanPurpose, startDateFixed, endDateFixed)
        return redirect("main:lease")


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
