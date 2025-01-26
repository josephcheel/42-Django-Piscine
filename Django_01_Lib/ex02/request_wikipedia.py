import requests 
import json 
import dewiki 
import sys

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('Usage: python request_wikipedia.py <title>')
		sys.exit(1)
	title = sys.argv[1]
	url = f'https://en.wikipedia.org/w/api.php'
	params = {
        "action": "query",
        "prop": "revisions",
        "rvprop": "content",
        "titles": title,
        "format": "json",
        "formatversion": 2
    }
	try:
		response = requests.get(url, params=params)
		data = response.json()
	except Exception as e:
		print(e, file=sys.stderr)
		sys.exit(1)
	try:
		content = data["query"]["pages"][0]["revisions"][0]["content"]
	except KeyError:
		print("Page not found", file=sys.stderr)
		sys.exit(1)
	
	# filename = title.replace(' ', '_') + '.wiki'
	filename = title + '.wiki'
	no_format_content = dewiki.from_string(content)

	try:
		with open(filename, 'w') as f:
			f.write(no_format_content)
	except Exception as e:
		print(e, file=sys.stderr)
		sys.exit(1)
	

	