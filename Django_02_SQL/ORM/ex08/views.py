from django.shortcuts import render
from django.http import HttpResponse
from django.templatetags.static import static
import psycopg2

# Create your views here.
def init(request):
	try: 
		connection = psycopg2.connect(
			dbname="djangotraining",
			user="djangouser",
			password="secret",
			host="localhost",
			port="5432"
		)
		cursor = connection.cursor()

		cursor.execute("CREATE TABLE IF NOT EXISTS ex08_planets \
						(id SERIAL PRIMARY KEY, \
						name VARCHAR(64) UNIQUE NOT NULL, \
						climate VARCHAR, \
						diameter INTEGER, \
						orbital_period INTEGER, \
						population BIGINT, \
						rotation_period INTEGER, \
						surface_water REAL, \
						terrain VARCHAR(128) \
					)")
		connection.commit()

		cursor.execute("CREATE TABLE IF NOT EXISTS ex08_people \
						(id SERIAL PRIMARY KEY, \
						name VARCHAR(64) UNIQUE NOT NULL, \
						birth_year VARCHAR(32), \
						gender VARCHAR(32), \
						eye_color VARCHAR(32), \
						hair_color VARCHAR(32), \
						height INTEGER, \
						mass REAL, \
						homeworld VARCHAR(64), \
						FOREIGN KEY(homeworld) REFERENCES ex08_planets(name) ON DELETE CASCADE ON UPDATE CASCADE \
					)")
		connection.commit()

		cursor.close()
		connection.close()
	except Exception as e:
		HttpResponse(f"Error: {e}")
	return HttpResponse("OK")

def parse_people_csv(line):
	line = line.split('\t')
	people = {
		'name': line[0] if line[0] != 'NULL' else None,
		'birth_year': line[1] if line[1] != 'NULL' else None,
		'gender': line[2] if line[2] != 'NULL' else None,
		'eye_color': line[3] if line[3] != 'NULL' else None,
		'hair_color': line[4] if line[4] != 'NULL' else None,
		'height': line[5] if line[5] != 'NULL' else None,
		'mass': line[6] if line[6] != 'NULL' else None,
		'homeworld': line[7] if line[7] != 'NULL' else None
	}

	return people

def parse_planets_csv(line):
	line = line.split('\t')
	planets = {
		'name': line[0] if line[0] != 'NULL' else None,
		'climate': line[1] if line[1] != 'NULL' else None,
		'diameter': line[2] if line[2] != 'NULL' else None,
		'orbital_period': line[3] if line[3] != 'NULL' else None,
		'population': line[4] if line[4] != 'NULL' else None,
		'rotation_period': line[5] if line[5] != 'NULL' else None,
		'surface_water': line[6] if line[6] != 'NULL' else None,
		'terrain': line[7] if line[7] != 'NULL' else None
	}

	return planets

def populate(request):
	ret_content = ""

	connection = psycopg2.connect(
				dbname="djangotraining",
				user="djangouser",
				password="secret",
				host="localhost",
				port="5432"
			)
	cursor = connection.cursor()

	try: 
		file_path = "." + static('ex08/planets.csv')
		with open(file_path, 'r') as f:
			num_lines = sum(1 for _ in f)
			f.seek(0) 
			cursor.copy_from(f, 'ex08_planets', sep='\t', columns=('name', 'climate', 'diameter', 'orbital_period', 'population', 'rotation_period', 'surface_water', 'terrain'), null='NULL')


			print('cursor.rowcount', cursor.rowcount)
			print('num_lines', num_lines)
			ret_content += "OK <br>" * cursor.rowcount
			connection.commit()
	except Exception as e:
		ret_content += f"Error: {e}<br>"
	
	try: 
		file_path = "." + static('ex08/people.csv')
		with open(file_path, 'r') as f:
			num_lines = sum(1 for _ in f)
			f.seek(0)
			cursor.copy_from(f, 'ex08_people', sep='\t', columns=('name', 'birth_year', 'gender', 'eye_color', 'hair_color', 'height', 'mass', 'homeworld'), null='NULL')
			print('cursor.rowcount', cursor.rowcount)
			print('num_lines', num_lines)
			ret_content += "OK <br>" * cursor.rowcount
			print(cursor)
			connection.commit()
	except Exception as e:
		ret_content += f"Error: {e}<br>"
	
	
	return HttpResponse(ret_content)

def display(request):
	try:
		connection = psycopg2.connect(
				dbname="djangotraining",
				user="djangouser",
				password="secret",
				host="localhost",
				port="5432"
		)
		cursor = connection.cursor()

		cursor.execute("SELECT ex08_people.name , ex08_planets.climate, ex08_people.homeworld \
						FROM ex08_planets \
						FULL OUTER JOIN ex08_people \
						ON ex08_planets.name = ex08_people.homeworld \
						WHERE ex08_planets.climate like '%windy%';")

		people = cursor.fetchall()	
		people.sort()
	except Exception as e:
		return HttpResponse(f"<h1>No data availeable</h1>")

	return render(request, 'ex08/display.html', {'people': people})