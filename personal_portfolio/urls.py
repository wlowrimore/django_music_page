"""
URL configuration for personal_portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from users import views as user_views
from disclosures import views as disclosure_views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path("admin/", admin.site.urls),
    path('', include('users.urls')),
    path('about/', user_views.about, name='about'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('profile/<int:user_id>/', user_views.profile_view, name='profile_detail'),
    # path('password_reset', user_views.password_reset_request, name='password_reset'),
    path("projects/", include("projects.urls")),
    path("contact/", include("contact.urls")),
    path("blog/", include("blog.urls")),
    path('privacy/', disclosure_views.privacy, name='privacy'),
    path('terms/', disclosure_views.terms, name='terms')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
