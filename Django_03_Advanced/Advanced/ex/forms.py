from django import forms

from .models import Article

class PublishArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ['title', 'synopsis', 'content']