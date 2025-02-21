from django.shortcuts import render
from django.http import HttpResponse
from ex09.models import Planets, People

# Create your views here.
def display(request):
	characters = People.objects.select_related('homeworld').filter(
		homeworld__climate__icontains='windy'
	).order_by('name')
	print(characters)
	for character in characters:
		print(character.homeworld.name, character.homeworld.climate)

	return render(request, 'ex09/display.html',{'characters': characters})