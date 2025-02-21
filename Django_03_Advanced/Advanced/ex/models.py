from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# • Article: Content of the article and a few metadata. It must feature the following
# fields:
# ◦ title: Article’s title. Character chain 64 max size. Non null.
# ◦ author: Article’s author. References a record of the User model. Non null.
# ◦ created: Creation’s complete date and time. Must be automatically filled
# when created. Non null.
# ◦ synopsis: Article’s abstract. Character chain. Max size 312. Non null.
# ◦ content: The article. It’s a text type. Non null.
# The __str()__ method must be ’overrode’ to send ’title’
# 7
# Training Python-Django - 3 Advanced
# • UserFavouriteArticle: User’s favorite articles. Must feature the following fields:
# ◦ user: References a record of the User model. Non null.
# ◦ article: References a record of the Article model. Non null.
# The __str()__ method must be overridden to send ’title’ included in the Article
# model.
class Article(models.Model):
	title = models.CharField(max_length=64, null=False, blank=False)
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")
	created = models.DateTimeField(auto_now_add=True, null=False)
	synopsis = models.CharField(max_length=312, blank=False)
	content = models.TextField(blank=False)
	def __str__(self):
		return self.title
	
class UserFavouriteArticle(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="fav_article", blank=False)
	article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="favorited_by", blank=False)
	def __str__(self):
		return 