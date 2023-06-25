from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "w-full outline-none border border-gray-300 rounded-sm my-4 py-1 px-2 w-full",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "w-full outline-none border border-gray-300 rounded-sm my-4 py-1 px-2 w-full",
            "placeholder": "Leave a comment!"
        })
    )
