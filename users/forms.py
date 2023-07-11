from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101, widget=forms.TextInput(attrs={
        'class': 'w-full border border-gray-300 rounded px-2 text-gray-800'
    }))
    last_name = forms.CharField(max_length=101, widget=forms.TextInput(attrs={
        'class': 'w-full border border-gray-300 rounded px-2 text-gray-800'
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'w-full border border-gray-300 rounded px-2 text-gray-800'
    }))

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'w-full border border-gray-300 rounded px-2 text-gray-800'
        self.fields['password1'].widget.attrs['class'] = 'w-full border border-gray-300 rounded px-2 text-gray-800'
        self.fields['password2'].widget.attrs['class'] = 'w-full border border-gray-300 rounded px-2 text-gray-800'


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
        attrs={'class': 'w-full border border-gray-300 rounded px-2 text-gray-800'
               }))
    password = forms.CharField(max_length=50, required=True,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'w-full border border-gray-300 rounded px-2 text-gray-800'
                                          }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'remember_me']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'description', 'profile_img']


class ContactForm(forms.Form):
    fullname = forms.CharField(max_length=101, required=True, widget=forms.TextInput(attrs={
        'class': 'w-full border border-gray-300 rounded px-2 text-gray-800'
    }))
    subject = forms.CharField(max_length=60, required=True, widget=forms.TextInput(attrs={
        'class': 'w-full border border-gray-300 rounded px-2 text-gray-800'
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'w-full border border-gray-300 rounded px-2 text-gray-800'
    }))
    message = forms.CharField(max_length=500, required=True, widget=forms.Textarea(attrs={
        'class': 'w-full border border-gray-300 rounded px-2 text-gray-800'
    }))
