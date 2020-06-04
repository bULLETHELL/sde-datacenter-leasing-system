from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import widgets, ModelForm
from django.forms.widgets import TextInput, PasswordInput, DateInput
from .models import InventoryItem, Loan

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

class LeaseForm(forms.Form):
    itemId = forms.IntegerField(widget=TextInput(attrs={'readonly': 'readonly'}))
    loanedItem = forms.CharField(widget=TextInput(attrs={'readonly': 'readonly'}))
    loanStartDate = forms.DateField(widget=DateInput())
    loanEndDate = forms.DateField(widget=DateInput(attrs={'readonly': 'readonly'}))
    loaningUser = forms.CharField(widget=TextInput(attrs={'readonly': 'readonly'}))
    loanPurpose = forms.CharField(widget=TextInput(attrs={'placeholder' : 'Purpose for loan'}))
        
    
    """ class Meta:
        model = Loan
        fields = 'id', 'loanedItem', 'loanStartDate', 'loanEndDate', 'loaningUser', 'loanPurpose'
        widgets = {
            'loanedItem': TextInput(attrs={'readonly': 'readonly'}),
            'loanStartDate': TextInput(attrs={'readonly':'readonly'}),
            'loanEndDate': DateInput,
            'loaningUser': TextInput(attrs={'readonly':'readonly'}),
            'loanPurpose': TextInput(attrs={'placeholder': 'Purpose for loan'})
        }

    def save(self, commit=True):
        loan = super(LeaseForm, self).save(commit=False)
        item = InventoryItem.objects.get(pk = 'id')

        loan.loanedItem = item
        item.itemAvailable = False

        if commit:
            loan.save() """


        
        

