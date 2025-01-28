from django.shortcuts import render, redirect
from django.http import HttpResponse
import psycopg2

# Create your views here.
def init(request):
	try:
		conn = psycopg2.connect(
			dbname="djangotraining",
			user="djangouser",
			password="secret",
			host="localhost",
			port="5432"
		)
		cursor = conn.cursor()
		
		cursor.execute("CREATE TABLE IF NOT EXISTS ex04_movies \
				 (title VARCHAR(64) UNIQUE NOT NULL, \
				 episode_nb INT PRIMARY KEY, opening_crawl TEXT, \
				 director VARCHAR(32) NOT NULL, \
				 producer VARCHAR(128) NOT NULL, \
				 release_date DATE NOT NULL)")
		conn.commit()
	except Exception as e:
		return HttpResponse("Error: {}".format(str(e)))
	return HttpResponse("OK!")



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
		conn = psycopg2.connect(
			dbname="djangotraining",
			user="djangouser",
			password="secret",
			host="localhost",
			port="5432"
		)
		cursor = conn.cursor()
	except Exception as e:
		return HttpResponse("Error: {}".format(str(e)))
	
	content = ""
	for e in episodes:
		cursor.execute("SELECT * FROM ex04_movies WHERE episode_nb=%s", (e['episode_nb'],))
		try:
			if cursor.fetchone() is not None:
				content += f"Episode {e['episode_nb']} already exists in the database.<br>"
			else:
				cursor.execute("INSERT INTO ex04_movies (title, episode_nb, director, producer, release_date) VALUES (%s, %s, %s, %s, %s)",
							(e['title'], e['episode_nb'], e['director'], e['producer'], e['release_date']))
				content += "OK!<br>"
			conn.commit()
		except Exception as e:
			return HttpResponse("Error: {}".format(str(e)))
	return HttpResponse(content)

def display(request):
	try: 
		conn = psycopg2.connect(
			dbname="djangotraining",
			user="djangouser",
			password="secret",
			host="localhost",
			port="5432"
		)
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM ex04_movies")
		episodes = cursor.fetchall()
	except Exception as e:
		return HttpResponse("No data available")
	return render(request, 'ex04/display.html', {'episodes': episodes})

def remove_title_line(title):
	try:
		conn = psycopg2.connect(
			dbname="djangotraining",
			user="djangouser",
			password="secret",
			host="localhost",
			port="5432"
		)
		cursor = conn.cursor()
		cursor.execute("DELETE FROM ex04_movies WHERE title=%s", (title,))
		conn.commit()
		return (redirect('ex04:remove'))
	except Exception as e:
		return HttpResponse("No data available")
			

def remove(request):
	if request.method == 'POST':
		return (remove_title_line(request.POST['title']))
	else:
		try: 
			conn = psycopg2.connect(
				dbname="djangotraining",
				user="djangouser",
				password="secret",
				host="localhost",
				port="5432"
			)
			cursor = conn.cursor()
			cursor.execute("SELECT title FROM ex04_movies")
			titles = cursor.fetchall()
		except Exception as e:
			return HttpResponse("No data available")
		if len(titles) == 0:
			return HttpResponse("No data available")
	return render(request, 'ex04/remove.html', { 'titles': titles })