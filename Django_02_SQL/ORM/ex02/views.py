from django.shortcuts import render
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
		
		cursor.execute("CREATE TABLE IF NOT EXISTS ex02_movies \
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
		for e in episodes:
			cursor.execute(f"INSERT INTO ex02_movies (title, episode_nb, director, producer, release_date) VALUES ('{e['title']}', '{e['episode_nb']}', '{e['director']}', '{e['producer']}', '{e['release_date']}')")
		conn.commit()
	except Exception as e:
		return HttpResponse("Error: {}".format(str(e)))
	return HttpResponse("OK!")

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
		cursor.execute("SELECT * FROM ex02_movies")
		episodes = cursor.fetchall()
	except Exception as e:
		return HttpResponse("No data available")
	return render(request, 'ex02/display.html', {'episodes': episodes})