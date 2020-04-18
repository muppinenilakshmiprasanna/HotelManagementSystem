from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Reservation

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class Booking(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('guestFirstName', 'guestLastName', 'email', 'phonenumber', 'CheckIn', 'CheckOut',)
        widgets = {
        'CheckIn': forms.DateInput(attrs={'class': 'datepicker'}),
        'CheckOut': forms.DateInput(attrs={'class': 'datepicker'})
        }