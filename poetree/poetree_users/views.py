from django.shortcuts import render,redirect
# one class that extends 
#UserCreationForm so that we save the emal
from . forms import UserRegisterForm
from django.contrib.auth.models import User # using default user model
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} το poetree σε αποδέχεται\n πλέον μπορείς να δημοσιέυσεις μαζί μας τα ποιήματα σου!')
            return redirect('poetree_login')
    else:
        form = UserRegisterForm()
    
    context = {
        'title': 'εγγραφή',
        'usernames': User.objects.values_list('username',flat=True).order_by('username'),
        'form': form
    }

    return render(request, 'poetree_users/register.pug', context=context)

@login_required
def profile(request):
    context = {
        'title': 'προφίλ {user.username}',
        'usernames': User.objects.values_list('username',flat=True).order_by('username'),
    }
    return render(request, 'poetree_users/profile.html', context=context)