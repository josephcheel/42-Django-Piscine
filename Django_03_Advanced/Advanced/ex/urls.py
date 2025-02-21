from django.urls import path, include
from django.shortcuts import redirect, render

from django.shortcuts import HttpResponse

from . import views



urlpatterns = [
    path('', views.HomeRedirect.as_view(), name='home'),
	path('articles/', views.ArticleList.as_view() , name="articles"),
	path('login/', views.MyLoginView.as_view(), name='login'),
	path('publications/', views.UserPublicationsList.as_view(), name="publications"),
	path('detail/<int:article_id>/', views.ArticleDetails.as_view(), name="detail"),
	path('logout/', views.MyLogoutView.as_view(), name="logout"),
	path('favourites/', views.FavouritesList.as_view(), name="favourites"),
	path('register/', views.MyRegisterView.as_view(), name="register"),
	path('publish/', views.CreatePublish.as_view(), name="publish"),
	path('add/favourite/<int:article_id>/', views.AddFavourite.as_view(), name="add_favourite")
]
