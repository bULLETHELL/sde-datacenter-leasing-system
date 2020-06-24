from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .forms import NewUserForm, LoginForm, LeaseForm
from .models import InventoryItem, InventoryItemType, Loan, User, Reservation, Returns
from datetime import date
from django.contrib import messages


# Create your views here.
def homepage(request):
    return render(request=request,
                  template_name='main/home.html',
                  context={'loginForm': LoginForm, 'username': request.user.username})


def profile(request):
    return render(request=request,
                  template_name='main/profile.html',
                  context={'loginForm': LoginForm, 'change_password_form': PasswordChangeForm, 'username': request.user.username,
                           'cur_user_loans': Loan.objects.filter(loaningUser=request.user),
                           'reservations_for_cur_user': Reservation.objects.filter(reservedFor=request.user),
                           'reservations_by_cur_user': Reservation.objects.filter(reservingUser=request.user), })

def change_password_request(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password was successfully updated!")
            return redirect('main:profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'main/profile.html')


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
                           'leaseForm': LeaseForm, 'datetoday': todayFormatted, 'user': request.user,
                           'cur_user_loans': Loan.objects.filter(loaningUser=request.user)})


def reserve(request):
    today = date.today()
    todayFormatted = today.strftime("%d/%m/%Y")
    # todayList = todayFormatted.split('/')
    # todayFormattedCorrectly = f"{todayList[0]}-{todayList[1]}-{todayList[2]}"
    return render(request=request,
                  template_name='main/reservation.html',
                  context={'loginForm': LoginForm, 'inventoryItems': InventoryItem.objects.all,
                           'inventoryItemTypes': InventoryItemType.objects.all, 'loans': Loan.objects.all,
                           'leaseForm': LeaseForm, 'datetoday': todayFormatted, 'curUser': request.user,
                           'users': User.objects.all, 'cur_user_loans': Loan.objects.filter(loaningUser=request.user)})


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


def return_request(request):
    if request.method == 'POST':
        print(request.POST.get)
        loanedItem = InventoryItem.objects.get(pk=request.POST.get("return_button"))
        loan = Loan.objects.get(loanedItem=loanedItem)

        newReturn = Returns(loanedItem=loanedItem, loanStartDate=loan.loanStartDate, loanReturnDate=loan.loanEndDate,
                            returningUser=loan.loaningUser, loanPurpose=loan.loanPurpose)
        newReturn.save()
        print(loanedItem.itemSoftware.all())#morten din pik kig her
        loan.delete()
        loanedItem.itemAvailable = True
        loanedItem.save()
        messages.success(request, f"the loan {loan} has been returned")
        print(loanedItem, loan)
        return redirect("/")
    return redirect("/")


def lease_request(request):
    if request.method == 'POST':
        form = LeaseForm(request.POST)
        print(form.errors.as_data())
        if form.is_valid():
            itemId = form.cleaned_data.get('itemId')
            loanedItem = InventoryItem.objects.get(pk=itemId)
            loanStartDate = form.cleaned_data.get('loanStartDate')
            loanEndDate = form.cleaned_data.get('loanEndDate')
            loaningUser = form.cleaned_data.get('loaningUser')
            loanPurpose = form.cleaned_data.get('loanPurpose')

            startDateSplit = loanStartDate.split('/')
            endDateSplit = loanEndDate.split('/')
            startDateFixed = f"{startDateSplit[2]}-{startDateSplit[1]}-{startDateSplit[0]}"
            endDateFixed = f"{endDateSplit[2]}-{endDateSplit[1]}-{endDateSplit[0]}"

            newLoan = Loan(loanedItem=loanedItem, loanStartDate=startDateFixed, loanEndDate=endDateFixed,
                           loaningUser=User.objects.get(username=loaningUser), loanPurpose=loanPurpose)
            newLoan.save()
            loanedItem.itemAvailable = False
            loanedItem.save()
            messages.success(request, f"Loan successful, {loanedItem} loaned to {loaningUser}")
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
                messages.success(request, f"Logged in: {username}")
                return redirect('/')

    messages.error(request,
                   f"login failed, the login details provided were either wrong or the given user has not yet been activated, if the latter, contact helpdesk")
    return redirect('main:homepage')


def logout_request(request):
    logout(request)
    return redirect('main:homepage')


def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        print(form.errors.as_data())
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.error(request, "Waiting for admin to activate user, you wont be able to log in till then")
            messages.success(request, f"New account created: {username}")
            return redirect('main:homepage')

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
            return redirect('main:homepage')

    form = NewUserForm
    return render(request=request,
                  template_name='main/register.html',
                  context={'form': form, 'loginForm': LoginForm})
