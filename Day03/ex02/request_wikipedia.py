import sys
import json
import requests
import dewiki

def	get_content(page : str):
	url = "https://fr.wikipedia.org/w/api.php?"
	query = {
		'action': 'parse',
		'page': page,
		'format': 'json',
		'prop': 'wikitext',
		'redirects': True
	}
	headers = {
		'User-Agent': '42Bot/0.0 (tanguy.bourdeau@42.fr)'
	}
	rep = requests.get(url, query, headers=headers)
	dict = rep.json()
	if 'error' in dict.keys():
		raise Exception("Error : The asked page does not exist on Wikipedia.")
	return dewiki.from_string(dict['parse']['wikitext']['*'] )

def	request_wikipedia():
	if len(sys.argv) < 2:
		raise Exception("Error: You did not asked for any page.")
	if len(sys.argv) > 2:
		raise Exception("Error: You can only ask for one page at once")
	content : str = get_content(sys.argv[1])
	with open(sys.argv[1].lower().replace(' ', '_').strip() + ".wiki", 'w') as f:
		f.write(content)

if __name__ == "__main__":
	try:
		request_wikipedia()
	except Exception as e :
		print(str(e))