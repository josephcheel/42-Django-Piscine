from django.shortcuts import render
from django.http import HttpResponse
from ex07.models import Movies
from .forms import UpdateForm

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

	content = ""
	for e in episodes:
		if Movies.objects.filter(episode_nb=e['episode_nb']).exists():
			content += "Episode {} already exists<br>".format(e['episode_nb'])
		else:
			try:
				Movies.objects.create(
					title=e['title'],
					episode_nb=e['episode_nb'],
					director=e['director'],
					producer=e['producer'],
					release_date=e['release_date']
				)
			except Exception as e:
				return HttpResponse("Error: {}".format(str(e)))
			content += "OK<br>"
	return HttpResponse(content)
	
	
def display(request):
	try:
		episodes = Movies.objects.all()
	except Exception as e:
		return HttpResponse("No data available")
	if len(episodes) == 0:
		return HttpResponse("No data available")
	return render(request, 'ex07/display.html' , {'episodes': episodes})

def remove(request):
	if request.method == 'POST':
		if 'title' in request.POST:
			try:
				Movies.objects.filter(title=request.POST['title']).delete()
			except Exception as e:
				return HttpResponse("No data available")
		else:
			return HttpResponse("No data available")
	titles = Movies.objects.values_list('title', flat=True)
	if len(titles) == 0:
		return HttpResponse("No data available")
	return render(request, 'ex07/remove.html', {'titles': titles})

def update(request):
	if request.method == 'POST':
		if 'title' in request.POST and 'opening_crawl' in request.POST:
			try:
				movie = Movies.objects.get(title=request.POST['title'])
				movie.opening_crawl = request.POST['opening_crawl']
				movie.save()
			except Exception as e:
				return HttpResponse("No data available")
		else:
			return HttpResponse("No data available")
	titles = Movies.objects.values_list('title', flat=True)
	if len(titles) == 0:
		return HttpResponse("No data available")
	return render(request, 'ex07/update.html', {
		'form': UpdateForm(choices=titles),
		})