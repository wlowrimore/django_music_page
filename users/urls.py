from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, about, profile, register, profile_view, activate, password_change

urlpatterns = [
    path('', home, name='users-home'),
    path('about/', about, name='users-about'),
    path('register/', register, name='users-register'),
    path('profile', profile, name='users-profile'),
    path('profile/<int:user_id>/', profile_view, name='users-profile_detail'),
    path('activate/<uidb64>/<token>', activate, name='activate'),
    path('password_change', password_change, name='password_change'),
    # path('password_reset', password_reset_request, name='password_reset'),
    # path('reset/<uidb64>/<token>', passwordResetConfirm, name='password_reset_confirm'),
]

