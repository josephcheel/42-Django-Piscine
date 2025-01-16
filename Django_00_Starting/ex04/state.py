import sys

states = {
"Oregon" : "OR",
"Alabama" : "AL",
"New Jersey": "NJ",
"Colorado" : "CO"
}
capital_cities = {
"OR": "Salem",
"AL": "Montgomery",
"NJ": "Trenton",
"CO": "Denver"
}


def find_state(capital):
	for key1, value1 in capital_cities.items():
		if value1 == capital:
			for key2, value2 in states.items():
				if value2 == key1:
					return key2
	return "Unknown capital city"

if __name__ == '__main__':
	if len(sys.argv) == 2:
		print(find_state(sys.argv[1]))