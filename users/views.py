from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from django.views.decorators.http import require_http_methods

from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from .models import CustomUser, Profile


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


# def profile_details(request):
#     user = CustomUser.objects.all()
#     details = Profile.objects.all()
#
#     context = {
#         "user": user
#         "details": details
#     }
#
#     return render(request, 'profile_detail', context)
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
