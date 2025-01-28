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
						CONSTRAINT homeworld  \
							FOREIGN KEY(homeworld) \
								REFERENCES ex08_planets(name) \
					)")
		connection.commit()

		cursor.close()
		connection.close()
	except Exception as e:
		HttpResponse(f"Error: {e}")
	return HttpResponse("OK")

# The first must be named ex08_planets and include the following fields:
# ◦ id: serial, primary key
# ◦ name: unique, variable character chain, 64 byte maximum size, non null.
# ◦ climate: variable character chain.
# ◦ diameter: whole.
# ◦ orbital_period: whole.
# ◦ population: large whole.
# ◦ rotation_period: whole.
# ◦ surface_water: real.
# ◦ terrain: variable character chain, 128 bytes maximum size.

# The second one must be called ex08_people and include the following fields:
# ◦ id: serial, primary key.
# ◦ name: unique, variable character chain, 64 byte maximum size, non null.
# ◦ birth_year: variable character chain, 32 byte maximum size.
# ◦ gender: variable character chain, 32 byte maximum size.
# ◦ eye_color: variable character chain, 32 byte maximum size.
# ◦ hair_color: variable character chain, 32 byte maximum size.
# ◦ height: whole.
# ◦ mass: real.
# ◦ homeworld: variable character chain, 64 byte maximum size, foreign key, referencing the name column of the 08_planets table.

def populate(request):
	ret_content = ""
	
	planets_table = ['name', 'climate', 'diameter', 'orbital_period', 'population', 'rotation_period', 'surface_water', 'terrain']
	people_table = ['name', 'birth_year', 'gender', 'eye_color', 'hair_color', 'height', 'mass', 'homeworld']
	
	connection = psycopg2.connect(
				dbname="djangotraining",
				user="djangouser",
				password="secret",
				host="localhost",
				port="5432"
			)
	cursor = connection.cursor()

	file_path = "./" + static('ex08/planets.csv')
	with open(file_path, 'r') as f:
		for line in f.readlines():
			clean_line = line.replace("\t", ", ").replace("\n", "").strip()
			try:
				# Using parameterized queries to avoid SQL injection
				cursor.execute(f"""
					INSERT INTO ex08_planets ({', '.join(planets_table)}) 
					VALUES ({', '.join(['%s'] * len(planets_table))})
				""", clean_line.split(", "))
			except Exception as e:
				ret_content += f"Error inserting planet: {e}<br>"
	connection.commit()

	try:
		file_path = "./" + static('ex08/people.csv')
		with open(file_path, 'r') as f:
			content = f.readlines()
			for line in content:
				ret_content += line + "<br>"
	except Exception as e:
		ret_content += f"Error: {e}<br>"
	
	return HttpResponse(ret_content)

def display(request):
	return HttpResponse("OK")
