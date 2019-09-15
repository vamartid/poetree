from django.shortcuts import render,render_to_response,get_object_or_404 # html rednering!
from django.contrib.auth.models import User # using default user model
from . models import Poem # so that we can handle the Poem model
from django.contrib import messages#views creation
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

def home(request):
    rand_id = -1
    if Poem.objects.all().count() > 0:
        rand_id = Poem.objects.order_by('?')[0].pk
    
    context = {
        'title': 'αρχική',
        'usernames':User.objects.values_list('username',flat=True).order_by('username'),
        'rand_id' : rand_id
    }
    return render(request,'poetree_blog/home.pug',context=context)

def poems(request):
    context = {
        'title': 'ποιήματα',
        'usernames': User.objects.values_list('username',flat=True).order_by('username'),
        'posts': Poem.objects.all(),
    }
    return render(request,'poetree_blog/poems.pug',context=context)

class PoemListView(ListView):
    model = Poem
    template_name = 'poetree_blog/poems.pug'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by=7
    extra_context = {
        'title': 'όλα τα ποιήματα',
        'usernames': User.objects.values_list('username',flat=True).order_by('username'),
    }

class PoemDetailView(DetailView):
    model = Poem
    extra_context = {
        'title':'προβολή',
        'usernames': User.objects.values_list('username',flat=True).order_by('username'),
    }

class PoemCreateView(LoginRequiredMixin,CreateView):
    model = Poem
    fields = ['title','content']
    extra_context = {
        'title':'νέα δημιουργία',
        'usernames': User.objects.values_list('username',flat=True).order_by('username'),
    }
    #success_url = '/poems'
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PoemUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Poem
    fields = ['title','content']
    extra_context = {
        'title':'επεξεργασία',
        'usernames': User.objects.values_list('username',flat=True).order_by('username'),
    }

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
    def test_func(self):
        poem = self.get_object()
        if self.request.user == poem.author:
            return True
        False

class PoemDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Poem
    success_url = '/poems'

    extra_context = {
        'title':'διαγραφή',
        'usernames': User.objects.values_list('username',flat=True).order_by('username'),
    }
    def test_func(self):
        poem = self.get_object()
        if self.request.user == poem.author:
            return True
        False

class UserPoemListView(ListView):
    model = Poem
    template_name = 'poetree_blog/poems.pug'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by=7
    extra_context = {
        'title':'ποιήματα χρήστη',
        'usernames': User.objects.values_list('username',flat=True).order_by('username'),
        't2': True,
    }

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Poem.objects.filter(author=user).order_by('-date_posted')

def about(request):
    context = {
        'title': 'σχετικά',
        'usernames':User.objects.values_list('username',flat=True).order_by('username'),
    }
    return render(request,'poetree_blog/about.pug',context=context)

