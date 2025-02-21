from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView
from django.views.generic import RedirectView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from .models import Article, UserFavouriteArticle

from .forms import PublishArticleForm

import json
import datetime

# Create your views here.

class HomeRedirect(RedirectView):
	permanent = True
	url = reverse_lazy('articles')

class MyLoginView(FormView):
	form_class = AuthenticationForm
	success_url = reverse_lazy('articles')
	template_name = 'articles_list.html'

	def form_valid(self, form):
		user = authenticate(self.request, username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
		if user is not None:
			login(self.request, user)
			return redirect(self.success_url)
		return self.form_invalid(form)


class ArticleList(MyLoginView, ListView):
	model = Article
	template_name = 'articles_list.html'
	context_object_name = 'articles'
	success_url = reverse_lazy('home')
	ordering = ['-created']


class UserPublicationsList(LoginRequiredMixin, ListView):
	model = Article
	template_name = 'publications_list.html'
	context_object_name = 'articles'
	login_url = '/articles/'
	redirect_field_name = 'next'
	ordering = ['-created']
	
	def get_queryset(self):
		return Article.objects.filter(author=self.request.user)

class ArticleDetails(LoginRequiredMixin, DetailView):
	model = Article
	pk_url_kwarg = 'article_id'
	template_name = 'article_details.html'
	context_object_name = 'article'
	login_url = '/articles/'
	redirect_field_name = 'next'


class MyLogoutView(RedirectView):
	def get(self, request):
		if request.user.is_authenticated:
			logout(request)
		return redirect('home')

class FavouritesList(LoginRequiredMixin, ListView):
	model = UserFavouriteArticle
	template_name = 'favourites_list.html'
	context_object_name = 'articles'
	login_url = '/articles/'
	redirect_field_name = 'next'
	ordering = ['-created']

	def get_queryset(self):
		return UserFavouriteArticle.objects.filter(user=self.request.user)
	
class MyRegisterView(CreateView):
	form_class = UserCreationForm
	template_name = 'register.html'
	success_url = reverse_lazy('home')

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('articles')
		return super().get(request, *args, **kwargs)
	def form_valid(self, form):
		if not self.request.user.is_authenticated:
			return super().form_valid(form)
		else:
			return redirect('articles')


class CreatePublish(LoginRequiredMixin, CreateView):
	form_class = PublishArticleForm
	template_name = 'article_publish.html'
	success_url = reverse_lazy('articles')
	login_url = '/articles/'
	redirect_field_name = 'next'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class AddFavourite(LoginRequiredMixin, CreateView):
	model = UserFavouriteArticle
	fields = []
	login_url = '/articles/'
	redirect_field_name = 'next'
	http_method_names = ['post']
	
	def form_valid(self, form):
		article_id = self.kwargs.get('article_id')
		try:
			article = Article.objects.get(id=article_id)
			if UserFavouriteArticle.objects.filter(user=self.request.user, article=article).exists():
				return JsonResponse({'error': 'Article already in favourites'}, status=400)
			form.instance.article = article
			form.instance.user = self.request.user 
		except Article.DoesNotExist:
			return JsonResponse({'error': 'Article not found'}, status=404)
		form.save()
		return redirect('detail', article_id=article_id)

	def form_invalid(self, form):
		return JsonResponse({'error': 'Invalid data'}, status=400)

		

