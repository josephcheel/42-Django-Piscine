from django import forms
from .models import Planets, People, Movies

class searchCharacterForm(forms.Form):
	minimum_release_date = forms.DateField(label="Minimum release date", required=True, widget=forms.DateInput(attrs={'type': 'date'}))
	maximum_release_date = forms.DateField(label="Maximum release date", required=True, widget=forms.DateInput(attrs={'type': 'date'}))

	planet_diameter = forms.IntegerField(label="Planet diameter", required=True, min_value=0)
	distinct_genders = People.objects.values_list('gender', flat=True).distinct()
	character_gender = forms.MultipleChoiceField(
		label="Character Gender", 
		required=True, 
		choices=[(gender, gender) for gender in distinct_genders]
	)
