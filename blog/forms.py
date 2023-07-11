from django import forms
from users.models import CustomUser


class CommentForm(forms.Form):
    author = CustomUser.username

    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "w-full outline-none border border-gray-300 rounded-sm my-4 py-1 px-2 w-full",
            "placeholder": "Leave a comment!"
        })
    )
