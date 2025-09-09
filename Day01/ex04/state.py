import sys

def state(capital : str):
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
	states = {y : x for x, y in states.items()}
	capital_cities = {y : x for x, y in capital_cities.items()}
	print (states.get(capital_cities.get(capital, None), "Unknown capital city"))


if __name__ == "__main__":
	if len(sys.argv) == 2:
		state(sys.argv[1])
