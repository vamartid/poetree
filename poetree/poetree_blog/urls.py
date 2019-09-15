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
from django.urls import path
from . import views
from .views import (
    PoemListView,
    PoemDetailView,
    PoemCreateView,
    PoemUpdateView,
    PoemDeleteView,
    UserPoemListView,
)
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', TemplateView.as_view(template_name='home.html'), name='home'), # new
    #path('registration/', include('django.contrib.auth.urls')), # new
    path('',views.home, name='poetree_home'),
    path('poems/',PoemListView.as_view(), name='poetree_poems'),
    path('user/<str:username>',UserPoemListView.as_view(), name='poetree_user_poems'),
    path('poems/<int:pk>/',PoemDetailView.as_view(template_name="poetree_blog/poem_detail.pug"), name='poetree_poem_detail'),
    path('poems/new/',PoemCreateView.as_view(template_name="poetree_blog/poem_form.pug"), name='poetree_poem_create'),
    path('poems/<int:pk>/update/',PoemUpdateView.as_view(template_name="poetree_blog/poem_form.pug"), name='poetree_poem_update'),
    path('poems/<int:pk>/delete/',PoemDeleteView.as_view(template_name="poetree_blog/poem_confirm_delete.pug"), name='poetree_poem_delete'),
    path('about/',views.about, name='poetree_about'),
]
#urlpatterns +=staticfiles_urlpatterns()
