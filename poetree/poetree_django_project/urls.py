"""poetree_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path,include
from poetree_users import views as poetree_users

from django.contrib.auth.models import User # using default user model for login,logout views
urlpatterns = [
    #admin
    path('admin/', admin.site.urls),
    #register
    path('register/', poetree_users.register, name='poetree_register'),
    #login passing data for sidebar
    path('login/', auth_views.LoginView.as_view(template_name='poetree_users/login.pug',
    extra_context = {
        'title': 'είσοδος',
        'usernames': User.objects.values_list('username',flat=True).order_by('username'),
    }), name='poetree_login'),
    #logout passing data for sidebar
    path('logout/', auth_views.LogoutView.as_view(template_name='poetree_users/logout.pug',
    extra_context = {
        'title': 'έξοδος',
        'usernames': User.objects.values_list('username',flat=True).order_by('username'),
    }), name='poetree_logout'),
    #user profile
    #path('profile/',poetree_users.profile, name='poetree_profile'),
    #other paths (home, about, full post view)
    path('', include('poetree_blog.urls')),
]
