from django.shortcuts import render
from django.http import HttpResponse
from ex03.models import Movies

# Create your views here.
def populate(request):
	episodes = [
		{
			'episode_nb': 1,
			'title': "The Phantom Menace",
			'director': "George Lucas",
			'producer': "Rick McCallum",
			'release_date': "1999-05-19"
		},
		{
			'episode_nb': 2,
			'title': "Attack of the Clones",
			'director': "George Lucas",
			'producer': "Rick McCallum",
			'release_date': "2002-05-16"
		},
		{
			'episode_nb': 3,
			'title': "Revenge of the Sith",
			'director': "George Lucas",
			'producer': "Rick McCallum",
			'release_date': "2005-05-19"
		},
		{
			'episode_nb': 4,
			'title': "A New Hope",
			'director': "George Lucas",
			'producer': "Gary Kurtz, Rick McCallum",
			'release_date': "1977-05-25"
		},
		{
			'episode_nb': 5,
			'title': "The Empire Strikes Back",
			'director': "Irvin Kershner",
			'producer': "Gary Kurtz, Rick McCallum",
			'release_date': "1980-05-17"
		},
		{
			'episode_nb': 6,
			'title': "Return of the Jedi",
			'director': "Richard Marquand",
			'producer': "Howard G. Kazanjian, George Lucas, Rick McCallum",
			'release_date': "1983-05-25"
		},
		{
			'episode_nb': 7,
			'title': "The Force Awakens",
			'director': "J. J. Abrams",
			'producer': "Kathleen Kennedy, J. J. Abrams, Bryan Burk",
			'release_date': "2015-12-11"
		}
	]
	try:
		for episode in episodes:
			Movies.objects.create(
				title=episode['title'],
				episode_nb=episode['episode_nb'],
				director=episode['director'],
				producer=episode['producer'],
				release_date=episode['release_date']
			)
	except Exception as e:
		return HttpResponse("Error: {}".format(str(e)))
	return HttpResponse("OK!")
	
	
def display(request):
	try:
		episodes = Movies.objects.all()
	except Exception as e:
		return HttpResponse("No data available")
	if len(episodes) == 0:
		return HttpResponse("No data available")
	return render(request, 'ex03/display.html' , {'episodes': episodes})