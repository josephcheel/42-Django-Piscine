from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser
class AddTipForm(forms.Form):
	content = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}), max_length=200)
	# author = forms.CharField(max_length=50)

class CreateUserForm(UserCreationForm):
	class Meta:
		model = CustomUser
		fields = ['username', 'password1', 'password2']