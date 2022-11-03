
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.forms import TextInput, DateInput, Select

from userextend.models import UserExtend


class UserExtendForm(UserCreationForm): #sign up
    class Meta:
        model = UserExtend
        fields = ['first_name', 'last_name', 'email_address', 'username', 'gender', 'birthday', 'account', 'phone']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'email_address': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your username'}),
            'gender': Select(attrs={'class': 'form-control'}),
            'birthday': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'account': Select(attrs={'class': 'form-control'}),
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
        fields = ['username', 'email']

        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your username'}),
            'email': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
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