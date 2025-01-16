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
	return None

def find_city(state):
	if state in states:
		return capital_cities[states[state]]
	else:
		return None

if __name__ == '__main__':
	if len(sys.argv) == 2:
		cities = ''.join(sys.argv[1]).split(',')
		for city_or_state in cities:
			city_or_state = city_or_state.strip().title()
			if city_or_state == '':
				continue
			elif find_city(city_or_state) is not None:
				print(f"{find_city(city_or_state)} is the capital of {city_or_state}")
			elif find_state(city_or_state) is not None:
				print(f"{city_or_state} is the capital of {find_state(city_or_state)}")
			else:
				print(f"{city_or_state} is neither a capital city nor a state")