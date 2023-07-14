from django.urls import path
from .views import home, about, profile, register, profile_view

urlpatterns = [
    path('', home, name='users-home'),
    path('about/', about, name='users-about'),
    path('register/', register, name='users-register'),
    path('profile', profile, name='users-profile'),
    path('profile/<int:user_id>/', profile_view, name='users-profile_detail'),
]
