from elements import Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br 
from elem import Elem, Text

class	Page:
	def	__init__(self, element: Elem):
		self.element = element

	def	__str__(self):
		if self.is_valid() == True:
			res = str(self.element)
			if type(self.element) == Html:
				return res.replace("<html", "<!DOCTYPE html", 1)
			return res
		else:
			print("Sorry, this page is not valid. Can't display such a mess on screen.")
			return ''

	def	write_to_file(self, filename : str):
		if self.is_valid() == False:
			print("Sorry, this page is not valid. Can't write such a mess in a file.")
			return
		with open(filename, 'w') as f:
			f.write(str(self))

	def	check_content(self, element_list: list[Elem | Text], condition : bool = True):
		if condition == False:
			raise Exception(f"Error: {type(self.element)} does not respect its tag rules")
		for elem in self.element.content:
			if type(elem) not in element_list:
				raise Exception(f"Error: {type(self.element)} tag does not respect its tag rules")
		return True

	def	is_valid(self) -> bool:
		try:
			elem_type :		type = type(self.element)
			if isinstance(self.element, Elem) == False or elem_type == Elem:
				return False
			if elem_type == Html:
				if type(self.element.content[0]) != Head or type(self.element.content[1]) != Body or \
					len(self.element.content) != 2:
					raise Exception("Error: HTML tag is not strictly composed of a Head and a Body tag")
			if elem_type == Head and (type(self.element.content[0]) != Title or len(self.element.content) != 1):
				raise Exception ("Error: head tag does not contain an unique title tag.")
			if elem_type in [Body, Div]:
				self.check_content([H1, H2, Div, Table, Ul, Ol, Span, Text])
			if elem_type in [Title, H1, H2, Li, Th, Td] and (type(self.element.content[0]) != Text or len(self.element.content) != 1):
				raise Exception (f"Error: {elem_type.__name__} tag does not contain an unique text object.")
			if elem_type == P:
				self.check_content([Text])
			if elem_type == Span:
				self.check_content([Text, P])
			if elem_type in [Ul, Ol]:
				self.check_content([Li], (len(self.element.content) != 0))
			if elem_type == Tr:
				if type(self.element.content[0]) == Th:
					self.check_content([Th])
				if type(self.element.content[0]) == Td:
					self.check_content([Td])
			if elem_type == Table:
				self.check_content([Tr])
			return self.check_next_node(self.element)
		except Exception as e:
			if str(e) == 'list index out of range':
				print(f"Error: {type(self.element).__name__} tag does not respect its tag rules")
			else:
				print(e)
			return False
		
	def	check_next_node(self, elem: Elem):
		for content in elem.content:
			if isinstance(content, Elem) == True:
				next_node = Page(content)
				if next_node.is_valid() == False:
					return False
			elif type(content) != Text:
				return False
		return True





def	wrong_cv_test() -> Page:

	headers = Title(Text("A transcended CV"))
	head = Head(headers)
	
	table_headers = [Tr(Th(Text("Career Path"), {'colspan': "2"}), [Th(Text("Years")), Th(Text("42 Cursus"))])]
	table_rows = [
		Tr([Td(Text("2022")), Td(Text("Piscine"))]),
		Tr([Td(Text("2023")), Td(Text("Minishell"))]),
		Tr([Td(Text("2024")), Td(Text("Transcendance"))]),
		Tr([Td(Text("2025")), Td(Text("Internship"), {'style': "background-color: #424242;"})]),		
	]
	table = Table(table_headers + table_rows)

	unordered_list = Ul([
		Li(Text("Management")),
		Li(Text("Sense of commitment")),
		Li(Text("Logic")),
		Li(Text("Persistent")),
		Li(Text("Passionate")),
	])
	ordered_list = Ol([
		Li(Text("Sport")),
		Ul([
			Li(Text("Snowboard")),
			Li(Text("Bodybuilding")),
			Li(Text("Swimming")),
			Li(Text("Crossfit")),
			Li(Text("Tennis")),
			Li(Text("Climbing"))
		]),
		Li(Text("Scoutism")),
		Li(Text("Coding")),
		Ul([
			Li(Text("Python")),
			Li(Text("C")),
			Li(Text("C++")),
			Li(Text("JavaScript")),
			Li(Text("TypeScript")),
			Li(Text("HTML")),
			Li(Text("CSS"))
		]),
		Li(Text("Video Games")),
		Ul([
			Li(Text("League of Legends")),
			Li(Text("Super Smash Bros Ultimate")),
			Li(Text("Teamfight Tactics"))
		])
	])
	body = Body([H1(Text("Tanguy BOURDEAU")), table, H2(Text("Skills")), unordered_list, H2(Text("Hobbies")), ordered_list])
	return Page(Html([head, body], {'lang':"en"}))

def	cv_test() -> Page:
	headers = Title(Text("A transcended CV"))
	head = Head(headers)
	
	table_headers = [
		Tr(Th(Text("Career Path"), {'colspan': "2"})),
		Tr([Th(Text("Years")), Th(Text("42 Cursus"))])
	]
	table_rows = [
		Tr([Td(Text("2022")), Td(Text("Piscine"))]),
		Tr([Td(Text("2023")), Td(Text("Minishell"))]),
		Tr([Td(Text("2024")), Td(Text("Transcendance"))]),
		Tr([Td(Text("2025")), Td(Text("Internship"), {'style': "background-color: #424242;"})]),		
	]
	table = Table(table_headers + table_rows)

	unordered_list = Ul([
		Li(Text("Management")),
		Li(Text("Sense of commitment")),
		Li(Text("Logic")),
		Li(Text("Persistent")),
		Li(Text("Passionate")),
	])
	ordered_list = Ol([
		Li(Text("Sport")),
		Li(Text("Snowboard")),
		Li(Text("Bodybuilding")),
		Li(Text("Swimming")),
		Li(Text("Crossfit")),
		Li(Text("Tennis")),
		Li(Text("Climbing")),
		Li(Text("Scoutism")),
		Li(Text("Coding")),
		Li(Text("Python")),
		Li(Text("C")),
		Li(Text("C++")),
		Li(Text("JavaScript")),
		Li(Text("TypeScript")),
		Li(Text("HTML")),
		Li(Text("CSS")),
		Li(Text("Video Games")),
		Li(Text("League of Legends")),
		Li(Text("Super Smash Bros Ultimate")),
		Li(Text("Teamfight Tactics"))
	])
	body = Body([H1(Text("Tanguy BOURDEAU")), table, H2(Text("Skills")), unordered_list, H2(Text("Hobbies")), ordered_list])
	return Page(Html([head, body], {'lang':"en"}))

if __name__ == "__main__":
	wrong_simple_page = Page(Html([Head(), Body()]))
	simple_page = Page(Html([Head(Title(Text())), Body()]))
	wrong_body_page = Page(Body([H1(), H2(), Div(), Table(), Ul(), Ol(), Span(), Text("Hello friend !")]))
	body_page = Page(Body([H1(Text('h1 tag')), H2(Text('h2 tag')), Div(), Table(Tr(Td(Text("Td from a Tr from a Table from a Body"), {}))), Ul(Li(Text("Li in a Ul in a Body"))), Ol(Li(Text("Li in a Ul in a Body"))), Span(), Text("Hello friend !")]))
	print("WRONG BODY PAGE :")
	print(wrong_body_page)
	body_page.write_to_file("body_page.html")
	print("WRONG HTML PAGE IN A FILE:")
	wrong_simple_page.write_to_file("wrong_simple_page.html")
	print("Wrong span & P tags:\n", Page(Span(P(Span(Text())))))
	print("Span & P tags:\n", Page(Span([Text("I'm in a span"), P(Text("And a p tag")), P()])))
	wrong_cv = wrong_cv_test()
	wrong_cv.write_to_file("wrong_cv.html")
	cv = cv_test()
	cv.write_to_file("cv.html")
	print("SIMPLE PAGE IN SIMPLE PAGE:")
	print(Page(Html([Head(Title(Text())), Body([H1(Text('h1 tag')), H2(Text('h2 tag')), Div([H1(Text('h1 tag')), H2(Text('h2 tag')), Div(), Table(Tr(Td(Text("Td from a Tr from a Table from a Body"), {}))), Ul(Li(Text("Li in a Ul in a Body"))), Ol(Li(Text("Li in a Ul in a Body"))), Span(), Text("Hello friend !")]), Table(Tr(Td(Text("Td from a Tr from a Table from a Body"), {}))), Ul(Li(Text("Li in a Ul in a Body"))), Ol(Li(Text("Li in a Ul in a Body"))), Span(), Text("Hello friend !")])])))