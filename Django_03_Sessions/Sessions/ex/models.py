from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
from django.conf import settings

# Create your models here.

class CustomUser(AbstractUser):
	rep_points = models.IntegerField(default=0)
	class Meta:
		permissions = [
			("downvote_posts", "Can downvote posts"),
		]
	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		if self.rep_points >= 15:
			if not self.user_permissions.filter(codename='downvote_posts').exists():
				self.user_permissions.add(Permission.objects.get(codename='downvote_posts'))
		else:
			if self.user_permissions.filter(codename='downvote_posts').exists():
				self.user_permissions.remove(Permission.objects.get(codename='downvote_posts'))

		if self.rep_points >= 30:
			if not self.user_permissions.filter(codename='delete_tip').exists():
				self.user_permissions.add(Permission.objects.get(codename='delete_tip'))
		else:
			if self.user_permissions.filter(codename='delete_tip').exists():
				self.user_permissions.remove(Permission.objects.get(codename='delete_tip'))
		super().save(*args, **kwargs)


class Tip(models.Model):
	content = models.TextField()
	author = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	upvotes = models.IntegerField(default=0)
	upvoted_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='upvoted_tips')
	downvoted_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='downvoted_tips')
	downvotes = models.IntegerField(default=0)

