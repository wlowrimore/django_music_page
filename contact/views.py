from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            html = render_to_string('contact_form.html', {
                'full_name': full_name,
                'email': email,
                'subject': subject,
                'message': message,
            })

            send_mail('Subject here', 'Here is the message.', 'from@example.com',
                      ['wlowrimore@gmail.com'], html_message=html)
            messages.success(request, 'Your entry was validated and sent!')
            return redirect("contact")
    else:
        form = ContactForm()
    return render(request, 'contact.html', {
        'form': form
    })
