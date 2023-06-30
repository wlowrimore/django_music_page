from django.shortcuts import render, redirect
from .forms import ContactForm


def contact(request):
    form = ContactForm()
    return render(request, 'contact.html', {
        'form': form
    })
