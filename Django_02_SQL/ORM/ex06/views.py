from django.shortcuts import render, redirect
from django.http import HttpResponse
import psycopg2
from .forms import UpdateForm

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
		
		cursor.execute("CREATE TABLE IF NOT EXISTS ex06_movies \
				 (title VARCHAR(64) UNIQUE NOT NULL, \
				 episode_nb INT PRIMARY KEY, opening_crawl TEXT, \
				 director VARCHAR(32) NOT NULL, \
				 producer VARCHAR(128) NOT NULL, \
				 release_date DATE NOT NULL, \
				 created TIMESTAMP DEFAULT CURRENT_TIMESTAMP, \
				 updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP );\
				 ")
		cursor.execute("CREATE OR REPLACE FUNCTION update_changetimestamp_column() \
				RETURNS TRIGGER AS $$ \
				BEGIN \
				NEW.updated = now(); \
				NEW.created = OLD.created; \
				RETURN NEW; \
				END; \
				$$ language 'plpgsql'; \
				")
		cursor.execute("CREATE OR REPLACE TRIGGER update_films_changetimestamp BEFORE UPDATE \
				ON ex06_movies FOR EACH ROW EXECUTE PROCEDURE \
				update_changetimestamp_column(); \
				")
				  
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
		cursor.execute("SELECT * FROM ex06_movies WHERE episode_nb=%s", (e['episode_nb'],))
		try:
			if cursor.fetchone() is not None:
				content += f"Episode {e['episode_nb']} already exists in the database.<br>"
			else:
				cursor.execute("INSERT INTO ex06_movies (title, episode_nb, director, producer, release_date) VALUES (%s, %s, %s, %s, %s)",
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
		cursor.execute("SELECT * FROM ex06_movies")
		episodes = cursor.fetchall()
	except Exception as e:
		return HttpResponse("No data available")
	return render(request, 'ex06/display.html', {'episodes': episodes})

def update_crawl_line(title, crawl):
	try:
		conn = psycopg2.connect(
			dbname="djangotraining",
			user="djangouser",
			password="secret",
			host="localhost",
			port="5432"
		)
		cursor = conn.cursor()
		cursor.execute("UPDATE ex06_movies SET opening_crawl=%s WHERE title=%s", (crawl, title))
		conn.commit()
	except Exception as e:
		return HttpResponse("No data available")
	return redirect('ex06:update')

def update(request):
	if request.method == 'POST':
		try:
			conn = psycopg2.connect(
				dbname="djangotraining",
				user="djangouser",
				password="secret",
				host="localhost",
				port="5432"
			)
			cursor = conn.cursor()
			cursor.execute("SELECT title FROM ex06_movies")
			titles = cursor.fetchall()
			form = UpdateForm(request.POST, choices=titles)
			if form.is_valid():
				title = form.cleaned_data['title']
				crawl = form.cleaned_data['opening_crawl']
				return update_crawl_line(title, crawl)
		except Exception as e:
			return HttpResponse("No data available")
		return HttpResponse("No data available")
	try: 
		conn = psycopg2.connect(
			dbname="djangotraining",
			user="djangouser",
			password="secret",
			host="localhost",
			port="5432"
		)
		cursor = conn.cursor()
		cursor.execute("SELECT title FROM ex06_movies")
		titles = cursor.fetchall()
	except Exception as e:
		return HttpResponse("No data available")
	if len(titles) == 0:
		return HttpResponse("No data available")
	return render(request, 'ex06/update.html', {
		'form': UpdateForm(choices=titles),
		})