from django.shortcuts import render
from django.http import HttpResponse
import psycopg2

# Create your views here.
def index(request):
	try:
		conn = psycopg2.connect(
			dbname="djangotraining",
			user="djangouser",
			password="secret",
			host="localhost",
			port="5432"
		)
		cursor = conn.cursor()
		
		cursor.execute("CREATE TABLE IF NOT EXISTS ex00_movies \
				 (title VARCHAR(64) UNIQUE NOT NULL, \
				 episode_nb INT PRIMARY KEY, opening_crawl TEXT, \
				 director VARCHAR(32) NOT NULL, \
				 producer VARCHAR(128) NOT NULL, \
				 release_date DATE NOT NULL)")
		conn.commit()
	except Exception as e:
		return HttpResponse("Error: {}".format(str(e)))
	return HttpResponse("OK!")