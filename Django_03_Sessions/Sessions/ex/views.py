from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required

from .forms import AddTipForm, CreateUserForm
from django.contrib.auth import get_user
from .models import Tip, CustomUser
import random
import datetime
import time

def get_random_username(request):
    DELAY_TIME = 42

    user = get_user(request)
    if user.is_authenticated:
        return JsonResponse({'username': user.username, 'rep_points': user.rep_points})
    last_username_str = request.session.get('last_username')
    last_username = datetime.datetime.fromisoformat(last_username_str) if last_username_str else datetime.datetime.min

    if not request.session.get('username') or (datetime.datetime.now() - last_username) > datetime.timedelta(seconds=DELAY_TIME):
        request.session['username'] = random.choice(settings.RANDOM_USERNAMES)
        request.session['last_username'] = datetime.datetime.now().isoformat()
    return JsonResponse({'username': request.session.get("username", "")} )

def index(request):
    posts = Tip.objects.all()
    user =  get_user(request)

    for post in posts:
        post.is_upvoted = post.upvoted_users.filter(id=get_user(request).id).exists()
        post.is_downvoted = post.downvoted_users.filter(id=get_user(request).id).exists()


    context = {}
    context['username'] = request.session.get('username', '')
    context['form'] = AddTipForm()
    context['posts'] = posts
    if user.is_authenticated:
        context['has_delete_permission'] = user.has_perm('ex.delete_tip')
        context['has_downvote_permission'] = user.has_perm('ex.downvote_posts')
        context['rep_points'] = user.rep_points
    else:
        context['has_delete_permission'] = False
        context['has_downvote_permission'] = False
        context['rep_points'] = None
    return render(request, 'index.html', context)

def loginView(request):
    user = get_user(request)
    if user.is_authenticated:
        return redirect('index')
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            request.session['username'] = form.cleaned_data.get('username')
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Invalid username or password')
    context = {'username': request.session.get('username', ''), 'form': form}
    return render(request, 'login.html', context)

def registerView(request):
    user = get_user(request)
    if user.is_authenticated:
        return redirect('index')
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            request.session['username'] = form.cleaned_data.get('username')
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created successfully for user ' + user)
            
            return redirect('login')
    context = {'username': request.session.get('username', ''), 'form': form}
    return render(request, 'register.html', context)

def logoutRequest(request):
    logout(request)
    return redirect('login')

@login_required
def addTip(request):
    if request.method != 'POST':
        return redirect('index')
    form = AddTipForm(request.POST)
    if form.is_valid():
        content = form.cleaned_data.get('content')
        author = get_user(request).username
        try:
            Tip.objects.create(content=content, author=author)
            messages.success(request, 'Tip added successfully')
        except Exception as e:
            messages.error(request, f'Error adding tip: {e}')
    return redirect('index')

@login_required
def upvote(request, tip_id):
    tip = get_object_or_404(Tip, id=tip_id)
    user = get_user(request)
    
    author = get_object_or_404(CustomUser, username=tip.author)
    if tip.upvoted_users.filter(id=user.id).exists():
        tip.upvoted_users.remove(user)
        tip.upvotes -= 1
        author.rep_points -= 5
        author.save()
    else:
        if tip.downvoted_users.filter(id=user.id).exists():
            tip.downvoted_users.remove(user)
            tip.downvotes -= 1
            author.rep_points += 2
        tip.upvotes += 1
        tip.upvoted_users.add(user)
        author.rep_points += 5
        author.save()
    tip.save()
    return redirect('index')

@login_required
def downvote(request, tip_id):

    tip = get_object_or_404(Tip, id=tip_id)
    user = get_user(request)
    if user.username != tip.author and not user.has_perm('ex.downvote_posts'):
        messages.error(request, 'You are not authorized to downvote this tip')
        return redirect('index')
    
    author = get_object_or_404(CustomUser, username=tip.author)
    if tip.downvoted_users.filter(id=user.id).exists():
        tip.downvoted_users.remove(user)
        tip.downvotes -= 1
        author.rep_points += 2
        author.save()
    else:
        if tip.upvoted_users.filter(id=user.id).exists():
            tip.upvoted_users.remove(user)
            tip.upvotes -= 1
            author.rep_points -= 5
        tip.downvotes += 1
        author.rep_points -= 2
        author.save()
        tip.downvoted_users.add(user)
    tip.save()
    return redirect('index')

@login_required
def deleteTip(request, tip_id):
    tip = get_object_or_404(Tip, id=tip_id)
    if request.user.username == tip.author:
        author = get_user(request)
        author.rep_points -= tip.upvotes * 5
        author.rep_points += tip.downvotes * 2
        author.save()
        tip.delete()
        messages.success(request, 'Tip deleted successfully')
    elif request.user.has_perm('ex.delete_tip'):
        author = get_object_or_404(CustomUser, username=tip.author)
        author.rep_points -= tip.upvotes * 5 
        author.rep_points += tip.downvotes * 2
        author.save()
        tip.delete()
        messages.success(request, 'Tip deleted successfully')
    else:
        messages.error(request, 'You are not authorized to delete this tip')
    return redirect('index')