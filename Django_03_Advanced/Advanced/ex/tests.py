from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Article, UserFavouriteArticle

USERNAME = 'testuser'
PASSWORD = 'testpassword'

class FavouriteViewsTestCase(TestCase):
	def setUp(self):
		"""Set up test user before each test."""
		self.client = Client()
		User.objects.create_user(username=USERNAME, password=PASSWORD)

	def login_user(self):
		"""Logs in the test user."""
		login_status = self.client.login(username=USERNAME, password=PASSWORD)
		self.assertTrue(login_status, 'Login failed')

	def test_favourites_views_access_control(self):
		"""Tests that protected views require authentication."""
		protected_urls = ['/favourites/', '/publications/', '/publish/']

		for url in protected_urls:
			response = self.client.get('/en' + url)
			print('/en' + url)
			self.assertEqual(response.status_code, 302, f"Expected redirect for unauthenticated user accessing {url}")

		self.login_user()

		for url in protected_urls:
			response = self.client.get('/en' + url)
			self.assertEqual(response.status_code, 200, f"Expected 200 for authenticated user accessing {url}")

	def check_logged_in_cannot_access_register(self):
		"""Tests that logged in users cannot access the registration page."""
		self.login_user()
		response = self.client.get('/en/register/')
		self.assertEqual(response.status_code, 302, "Expected redirect for authenticated user accessing /register/")

	def test_user_cannot_submit_register(self):
		"""Tests that a user cannot submit the registration form."""

		self.login_user()
		response = self.client.post('/register/', {'username': USERNAME, 'password': PASSWORD})
		self.assertEqual(response.status_code, 302, "Expected redirect for POST to /register/")

	def test_user_cannot_add_same_article_twice(self):
		"""Tests that a user cannot add the same article to their favorites twice."""
		self.login_user()

		article = Article.objects.create(title='Test Article', content='Test Content', author=User.objects.get(username=USERNAME))

		response = self.client.post(f'/en/add/favourite/{article.id}/')
		self.assertEqual(response.status_code, 302, "Expected 302 for adding article to favorites")

		response = self.client.post(f'/en/add/favourite/{article.id}/')
		self.assertEqual(response.status_code, 400, "Expected 400 for adding same article to favorites again")


		favourites = UserFavouriteArticle.objects.filter(user=User.objects.get(username=USERNAME))
		self.assertEqual(favourites.count(), 1, "Expected only one favorite article")




# Create your tests here.
