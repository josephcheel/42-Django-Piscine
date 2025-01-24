import requests 
import json 
import dewiki 
import sys

if __name__ == '__main__':
	print(sys.argv)
	if len(sys.argv) != 2:
		print('Usage: python request_wikipedia.py <title>')
		sys.exit(1)
	title = sys.argv[1]
	url = f'https://en.wikipedia.org/w/api.php?action=query&format=json&titles={title}&prop=info'
	print(url)
	response = requests.get(url)
	data = response.json()
	print(data)
	# help(dewiki)