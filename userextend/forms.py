
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.forms import TextInput, DateInput, Select, CheckboxInput

from userextend.models import UserExtend


class UserExtendForm(UserCreationForm): #sign up
    class Meta:
        model = UserExtend
        fields = ['firstname', 'lastname', 'email_address', 'username', 'gender', 'birthday', 'seller','buyer', 'phone']

        widgets = {
            'firstname': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'lastname': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'email_address': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your username'}),
            'gender': Select(attrs={'class': 'form-control'}),
            'birthday': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'phone': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your phone number'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter '
                                                                                              'your password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your '
                                                                                              'password confirmation'})


class AuthenticationNewForm(AuthenticationForm): #log in

    class Meta:
        model = UserExtend
        fields = ['email_address', 'password']

        widgets = {
            'email_address': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email address'}),
            'password': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your password'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your password'})


class PasswordResetNewForm(PasswordResetForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your email'})


class SetPasswordNewForm(SetPasswordForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control',
                                                           'placeholder': 'Please enter your password'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control',
                                                           'placeholder': 'Please enter your password confirmation'})