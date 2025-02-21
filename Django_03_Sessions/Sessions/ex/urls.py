from django.urls import path

from .views import index, get_random_username, loginView, registerView, logoutRequest, addTip, upvote, downvote, deleteTip

urlpatterns = [
	path('', index, name='index'),
	path('get_random_username/', get_random_username, name='get_random_username'),
	path('login/', loginView, name='login'),
	path('register/', registerView, name='register'),
	path('logout/', logoutRequest, name='logout'),
	path('add_tip/', addTip, name='add_tip'),
	path('upvote/<int:tip_id>/', upvote, name='upvote'),
	path('downvote/<int:tip_id>/', downvote, name='downvote'),
	path('delete/<int:tip_id>/', deleteTip, name='delete_tip'),
]
