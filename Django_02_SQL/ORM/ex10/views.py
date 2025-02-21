from django.shortcuts import render
import datetime
# Create your views here.

from .models import Planets, People, Movies
from .forms import searchCharacterForm
import datetime

def form(request):
	if request.method == 'POST':
		form = searchCharacterForm(request.POST)
		if form.is_valid():
			minimum_release_date = form.cleaned_data['minimum_release_date']
			maximum_release_date = form.cleaned_data['maximum_release_date']
			planet_diameter = form.cleaned_data['planet_diameter']
			character_gender =  form.cleaned_data['character_gender']
			if minimum_release_date > maximum_release_date:
				print('Minimum release date must be less than maximum release date')
				return render(request, 'ex10/form.html', {'form': searchCharacterForm(), 'error': 'Minimum release date must be less than maximum release date'})

			people = People.objects.select_related('homeworld').filter(
				movies__release_date__gte=minimum_release_date,
				movies__release_date__lte=maximum_release_date,
				homeworld__diameter__gte=planet_diameter,
				gender__in=character_gender
			).prefetch_related('movies')

			print(people.query)
			print(people)
			for person in people:
				print(vars(person))
				# print(vars(person._prefetched_objects_cache['movies']))
				# for movie in person.movies:
				# 	print(vars(movie))
			return render(request, 'ex10/form.html', {'form': searchCharacterForm(), 'people': people})
		return render(request, 'ex10/form.html', {'form': searchCharacterForm()})
	return render(request, 'ex10/form.html', {'form': searchCharacterForm()})
