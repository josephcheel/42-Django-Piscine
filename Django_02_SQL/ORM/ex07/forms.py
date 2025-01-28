from django import forms

class UpdateForm(forms.Form):
    title = forms.ChoiceField(choices=[])
    opening_crawl = forms.CharField(label="opening_crawl")

    def __init__(self, *args, **kwargs):
        choices = kwargs.pop('choices', [])
        super().__init__(*args, **kwargs)
        self.fields['title'].choices =  [(choice, choice) for choice in choices]