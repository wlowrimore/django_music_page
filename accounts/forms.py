from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser
from django.core.validators import EmailValidator


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


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "w-full bg-gray-300 outline-none border border-red-400 my-4 py-1 px-2 w-full"
        })
    )

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'description']


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
