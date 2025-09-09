import sys

def capital_city(state : str):
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
	print(capital_cities.get(states.get(state, None), "Unknown state"))

if __name__ == "__main__":
	if len(sys.argv) == 2:
		capital_city(sys.argv[1])
