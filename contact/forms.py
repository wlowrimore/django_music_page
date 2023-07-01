from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=101, required=True, widget=forms.TextInput(attrs={
        'class': 'w-full border border-gray-300 rounded px-2 text-gray-800'
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'w-full border border-gray-300 rounded px-2 text-gray-800'
    }))
    subject = forms.CharField(max_length=60, required=True, widget=forms.TextInput(attrs={
        'class': 'w-full border border-gray-300 rounded px-2 text-gray-800'
    }))
    message = forms.CharField(max_length=500, required=True, widget=forms.Textarea(attrs={
        'class': 'w-full border border-gray-300 rounded px-2 text-gray-800',
        'rows': '9'
    }))
