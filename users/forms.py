from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm, PasswordResetForm

from .models import CustomUser, Profile


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    # Create a UserUpdateForm to update a username and email


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=101, widget=forms.TextInput(attrs={
        'class': 'w-full border border-gray-300 rounded px-1 mb-3 text-gray-800'
    }))
    last_name = forms.CharField(max_length=101, widget=forms.TextInput(attrs={
        'class': 'w-full border border-gray-300 rounded px-1 mb-3 text-gray-800'
    }))
    username = forms.CharField(help_text=False, widget=forms.TextInput(attrs={
        'class': 'w-full border border-gray-300 rounded px-1 mb-3 text-gray-800'
    }))

    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'w-full border border-gray-300 rounded px-1 mb-3 text-gray-800'
    }))

    # description = forms.CharField(widget=forms.Textarea(attrs={
    #     'class': 'w-full border border-gray-300 rounded px-1 mb-3 text-gray-800'
    # }))

    class Meta:
        model = CustomUser
        fields = ['username', 'email']
        help_texts = {
            'username': None,
        }

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'w-full border border-gray-300 rounded px-2 text-gray-800'


class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=101, widget=forms.TextInput(attrs={
        'class': 'w-full border border-gray-300 rounded px-2 text-gray-800'
    }))
    last_name = forms.CharField(max_length=101, widget=forms.TextInput(attrs={
        'class': 'w-full border border-gray-300 rounded px-2 text-gray-800'
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'w-full border border-gray-300 rounded px-2 text-gray-800'
    }))
    location = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full border border-gray-300 rounded px-2 text-gray-800'
    }))
    bio = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'w-full border border-gray-300 rounded px-2 text-gray-800'
    }))
    profile_img = forms.ImageField()

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'location', 'bio', 'profile_img']


class ChangePasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput)
    new_password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']


# class ChangePasswordForm(SetPasswordForm):
#     new_password1 = forms.CharField(widget=forms.PasswordInput)
#     new_password2 = forms.CharField(widget=forms.PasswordInput)
#
#     class Meta:
#         model = CustomUser
#         fields = ['new_password1', 'new_password2']


# class PasswordResetForm(PasswordResetForm):
#     email = forms.EmailField()
#
#     class Meta:
#         model = CustomUser()
#         fields = ['email']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
        attrs={'class': 'w-full border border-gray-300 rounded px-2 text-gray-800'
               }))
    password = forms.CharField(max_length=50, required=True,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'w-full border border-gray-300 rounded px-2 text-gray-800'
                                          }))

    # remember_me = forms.BooleanField(required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'password']


# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()
#     description = forms.CharField(widget=forms.Textarea)
#
#     class Meta:
#         model = get_user_model()
#         fields = ['first_name', 'last_name', 'email', 'description', 'profile_img']


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
