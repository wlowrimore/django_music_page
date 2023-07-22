from django.contrib.auth import get_user_model, update_session_auth_hash, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage

import users
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm, ChangePasswordForm
from .models import CustomUser
from .tokens import account_activation_token


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def activate(request, uidb64, token):
    user = CustomUser()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('login')
    else:
        messages.error(request, 'Activation link is invalid or has expired!')
    return redirect('/')


def activateEmail(request, user, to_email):
    mail_subject = 'Activate your user account.'
    message = render_to_string('template_activate_account.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f"Dear {user}, please check your email and click the activation link to complete "
                                  f"registration.")
    else:
        messages.error(request, f'Problem sending confirmation email to {to_email}, make sure you typed it correctly. ')


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('register')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UserRegistrationForm()

    return render(
        request=request,
        template_name="register.html",
        context={"form": form}
    )


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('')
    else:
        messages.error(request, 'User not found in database')
        return render(request, 'home.html')


@login_required
def profile(request, username=None):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been successfully updated')
            return redirect('profile')  # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user.profile)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    user = get_user_model().objects.filter(username=username).first()
    if user:
        form = UserUpdateForm(instance=user)
        form.fields['bio'].widget.attrs = {
            'class': 'bg-gray-200 p-2 text-light text-sm tracking-wide rounded-sm', 'rows': 10, 'max_length': 255}
        form.fields['first_name'].widget.attrs = {
            'class': 'bg-gray-200 py-1 px-2 text-light text-sm tracking-wide rounded-sm'}
        form.fields['last_name'].widget.attrs = {
            'class': 'bg-gray-200 py-1 px-2 text-light text-sm tracking-wide rounded-sm'}
        form.fields['email'].widget.attrs = {
            'class': 'bg-gray-200 py-1 px-2 text-light text-sm tracking-wide rounded-sm'}
        form.fields['location'].widget.attrs = {
            'class': 'bg-gray-200 py-1 px-2 text-light text-sm tracking-wide rounded-sm'}

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'profile.html', context)


@require_http_methods(['GET'])
def profile_view(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)

    context = {
        'user': user,
        'path': request.path
    }
    return render(request, 'profile_detail.html', context)


@login_required
def password_change(request):
    user = users.models.CustomUser(request.user)
    if request.method == 'POST':
        form = ChangePasswordForm(user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your password has been successfully changed.')
            return redirect('login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    form = ChangePasswordForm(user)
    return render(request, 'password_reset_confirm.html', {'form': form})
