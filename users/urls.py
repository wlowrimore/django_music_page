from django.urls import path
from .views import home, about, profile, register

urlpatterns = [
    path('', home, name='users-home'),
    path('about/', about, name='users-about'),
    path('register/', register, name='users-register'),
    path('profile/', profile, name='users-profile'),
]
