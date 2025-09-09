import sys

def	cap_states_lists():
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
	return (states, capital_cities)

def capital_city(state : str):
	states, capital_cities = cap_states_lists()
	reverse_states = {y : x for x, y in states.items()}
	states_upper = {key.upper() : val.upper() for key, val in states.items()}
	key_res = states_upper.get(state, None)
	if key_res == None:
		return(None)
	return(capital_cities[key_res], reverse_states[key_res])

def state(capital : str):
	states, capital_cities = cap_states_lists()
	reverse_states = {y : x for x, y in states.items()}
	capital_cities_upper = {y.upper() : x.upper() for x, y in capital_cities.items()}
	key_res = capital_cities_upper.get(capital, None)
	if key_res == None:
		return(None)
	return (capital_cities[key_res], reverse_states[key_res])

def	parsing_hub(arg : str):
	input_list = [val.strip() for val in arg.split(',')]
	for val in input_list:
		if val == '':
			continue
		elif state(val.upper()) != None:
			print(f"{state(val.upper())[0]} is the capital_city of {state(val.upper())[1]}")
		elif capital_city(val.upper()) != None:
			print(f"{capital_city(val.upper())[0]} is the capital city of {capital_city(val.upper())[1]}")
		else:
			print(f"{val} is neither a capital city nor a state")


if __name__ == "__main__":
	if len(sys.argv) == 2:
		parsing_hub(sys.argv[1])
