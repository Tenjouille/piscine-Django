from sys import argv
from requests import get
from bs4 import BeautifulSoup

def	findIntro(content : str):
	soup = BeautifulSoup(content, "html.parser")
	return soup.find_all('p')

def	invalid_next_url(link_tag):
	if 'href' not in link_tag.attrs or 'title' not in link_tag.attrs:
		return True
	if ':' in link_tag['title']:
		return True
	if research("https://en.wikipedia.org", link_tag['href']).reason != 'OK':
		return True
	return False

def extractLinks(content : str):
	pgraphs = findIntro(content)
	for pgraph in pgraphs:
		link_list = pgraph.find_all('a')
		if len(link_list) != 0:
			for link in link_list:
				if invalid_next_url(link):
					continue
				return link['href']
	return None

def	get_title(content : str):
	soup = BeautifulSoup(content, "html.parser")
	page_title = str(soup.title)[7:-20]
	return page_title

def	research(url, page : str):
	headers = {
		'User-Agent': '42Bot/0.0 (tanguy.bourdeau@42.fr)'
	}
	return get(url + page, headers=headers)


def	get_content(page : str):
	rep = research("https://en.wikipedia.org/wiki/", page)
	if rep.reason != 'OK':
		raise Exception("Error : The asked page does not exist on Wikipedia.")
	road = [page]
	title = get_title(rep.content)
	if title.lower() != page.lower():
		road.append(title)

	while True:
		if title == "Philosophy":
			return road
		href = extractLinks(rep.content)
		if href == None:
			raise Exception("It leads to a dead end !")
		rep = research("https://en.wikipedia.org", href)
		title = get_title(rep.content)
		if title in road:
			raise Exception("It leads to an infinite loop")
		road.append(title)

def	request_wikipedia():
	if len(argv) < 2:
		raise Exception("Error: You did not asked for any title.")
	if len(argv) > 2:
		raise Exception("Error: You can only ask for one page at once")
	road : list[str] = get_content(argv[1])
	for page in road:
		print(page)
	print(f"{len(road)} roads from {argv[1]} to philosophy !")

if __name__ == "__main__":
	try:
		request_wikipedia()
	except Exception as e :
		print(str(e))
