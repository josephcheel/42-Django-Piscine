from django import forms

class InputHistoryForm(forms.Form):
	line = forms.CharField(label="Add content to the history", max_length=100)
