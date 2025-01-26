import sys
import requests
from bs4 import BeautifulSoup, Comment



def get_response(url):
	# Get the html content of the given url
	try:
		response = requests.get(url)
	except Exception as e:
		print(e)
		sys.exit(1)
	return response



def get_link(url):
	response = get_response(url)
	html_parsed = BeautifulSoup(response.text, 'html.parser')
	for comment in html_parsed.find_all(string=lambda text: isinstance(text, Comment)):
		comment.extract()
	main = html_parsed.find('div', {'id': 'bodyContent'})
	# link = main.find('a')
	for a_tag in main.find_all('a', href=True):
		href = a_tag['href']
		if href.startswith('/wiki/') and ':' not in href:
			# Check if a_tag is a sub tag of table
			is_subtag_of_table = False
			parent = a_tag
			while parent:
				if parent.name == 'table':
					is_subtag_of_table = True
					break
				parent = parent.parent
			# Check if a_tag is a direct child of a <p> tag
			if not is_subtag_of_table and a_tag.find_parent('p'):
				return a_tag
	return None


class FindPhilosophy():
	def __init__(self):
		self.visited = []
		self.roads = 0
	def search_in_wiki(self, url):
		print(url.split('/')[-1])
		if url in self.visited:
			print('It leads to an infinite loop !')
			sys.exit(1)
		if url == 'https://en.wikipedia.org/wiki/Philosophy':
			# print('Philosophy')
			return print(f'{self.roads} roads from {sys.argv[1]} to Philosophy')
		else:
			link = get_link(url)
			if link is None:
				print('The article does not exist on Wikipedia')
				sys.exit(1)
			if link['href'] in self.visited:
				print('It leads to an infinite loop !')
				sys.exit(1)
			self.visited.append(link['href'])
			self.roads += 1
			self.search_in_wiki(f'https://en.wikipedia.org{link["href"]}')


if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('Help: Program to find the path to philosophy on Wikipedia from a given article')
		print('usage: python roads_to_philosophy.py <name of the wikipedia article>')
		sys.exit(1)
	if '\\' in sys.argv[1] or '/' in sys.argv[1]:
		print('Please provide the name of the wikipedia article without any path')
		sys.exit(0)
	search = FindPhilosophy()

	url = f'https://en.wikipedia.org/wiki/{sys.argv[1]}'
	search.search_in_wiki(url)