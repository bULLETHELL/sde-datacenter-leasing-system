from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.backends import AllowAllUsersModelBackend
from django import forms
from django.forms import widgets, ModelForm
from django.forms.widgets import TextInput, PasswordInput, DateInput
from .models import InventoryItem, Loan, Purpose


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "is_superuser", "is_staff", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.is_active = False
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'UNI-LOGIN'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'PASSWORD'}))


class LoanForm(forms.ModelForm):
    loanedItem = forms.CharField(initial=123)

    class Meta:
        model = Loan
        fields = ('loanedItem', 'loanEndDate', 'loaningUser', 'loanPurpose',)


class LeaseForm(LoanForm):
    itemName = forms.CharField()
    loanStartDate = forms.CharField()

    class Meta(LoanForm.Meta):
        fields = ('itemName', ) + LoanForm.Meta.fields
