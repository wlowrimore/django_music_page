from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm


def home(request):
    return render(request, 'accounts/home.html')


def about(request):
    return render(request, 'accounts/about.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def profile(request, username):
    if request.method == 'POST':
        user = request.user
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_form = form.save()

            messages.success(request, f'{user_form}, Your profile has been updated!')
            return redirect('profile', user_form.username)

        for error in list(form.errors.values()):
            messages.error(request, error)

    user = get_user_model().objects.filter(username=username).first()
    if user:
        form = UserUpdateForm(instance=user)
        form.fields['description'].widget.attrs = {
            'class': 'bg-gray-200 p-2 text-light text-sm tracking-wide', 'rows': 10}
        context = {'form': form}
        return render(request, 'accounts/profile.html', context)

    return redirect('home')
