from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "w-full px-2 border border-gray-400 focus:bg-white",
            "placeholder": "username",
        })
    )
    password = forms.CharField(
        max_length=60,
        widget=forms.PasswordInput(attrs={
            "class": "w-full border border-gray-300 rounded-sm my-4 py-1 px-2 w-full",
            "placeholder": "password",
        })
    )
