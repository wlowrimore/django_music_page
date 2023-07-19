from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm, PasswordResetForm

from .models import CustomUser, Profile


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(help_text=False, widget=forms.TextInput(attrs={
        'class': 'w-full border-b border-gray-400 px-1 mb-3 text-gray-800 focus:outline-none',
        'placeholder': 'username*'
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'w-full border-b border-gray-400 px-1 mb-3 text-gray-800 focus:outline-none',
        'placeholder': 'email address*'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs[
            'class'] = 'w-full border-b border-gray-400 text-gray-800 focus:outline-none'
        self.fields['password1'].widget.attrs[
            'placeholder'] = 'create password*'
        self.fields['password2'].widget.attrs[
            'class'] = 'w-full border-b border-gray-400 text-gray-800 focus:outline-none'
        self.fields['password2'].widget.attrs[
            'placeholder'] = 'confirm password'


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=101, widget=forms.TextInput(attrs={
        'class': 'w-full border-b border-gray-300 rounded px-1 mb-3 text-gray-800 focus:outline-none',
        'placeholder': 'first name*'
    }))
    last_name = forms.CharField(max_length=101, widget=forms.TextInput(attrs={
        'class': 'w-full border-b border-gray-300 rounded px-1 mb-3 text-gray-800 focus:outline-none',
        'placeholder': 'last name*'
    }))
    username = forms.CharField(help_text=False, widget=forms.TextInput(attrs={
        'class': 'w-full border-b border-gray-300 rounded px-1 mb-3 text-gray-800 focus:outline-none',
        'placeholder': 'username*'
    }))

    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'w-full border-b border-gray-300 rounded px-1 mb-3 text-gray-800 focus:outline-none',
        'placeholder': 'email address*'
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

        self.fields['username'].widget.attrs[
            'class'] = 'w-full border-b border-gray-300 rounded text-gray-800 focus:outline-none'


class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=101, widget=forms.TextInput(attrs={
        'class': 'w-full border-b border-gray-300 rounded text-gray-800 focus:outline-none',
        'placeholder': 'update first name'
    }))
    last_name = forms.CharField(max_length=101, widget=forms.TextInput(attrs={
        'class': 'w-full border-b border-gray-300 rounded text-gray-800 focus:outline-none',
        'placeholder': 'update last name'
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'w-full border-b border-gray-300 rounded text-gray-800 focus:outline-none',
        'placeholder': 'update email address'
    }))
    location = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full border-b border-gray-300 rounded text-gray-800 focus:outline-none',
        'placeholder': 'update location'
    }))
    bio = forms.CharField(max_length=254, widget=forms.Textarea(attrs={
        'class': 'w-full border-b border-gray-300 px-1 rounded text-gray-800 focus:outline-none',
        'rows': '2',
        'placeholder': 'update bio'
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


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(help_text=False, widget=forms.TextInput(attrs={
        'class': 'w-full border-b border-gray-400 px-1 mb-3 text-gray-800 focus:outline-none',
        'placeholder': 'username*'
    }))
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs[
            'class'] = 'w-full border-b border-gray-400 text-gray-800 focus:outline-none'
        self.fields['username'].widget.attrs[
            'placeholder'] = 'username*'
        self.fields['password'].widget.attrs[
            'class'] = 'w-full border-b border-gray-400 text-gray-800 focus:outline-none'
        self.fields['password'].widget.attrs[
            'placeholder'] = 'password*'


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
