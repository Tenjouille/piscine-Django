from elem import Elem, Text

class	Html(Elem):
	def	__init__(self, content = None, attr = {}, indent = ''):
		super().__init__('html', attr, content, 'double', indent=indent)

class	Head(Elem):
	def	__init__(self, content = None, attr = {}, indent = ''):
		super().__init__('head', attr, content, 'double', indent=indent)

class	Body(Elem):
	def	__init__(self, content = None, attr = {}, indent = ''):
		super().__init__('body', attr, content, 'double', indent=indent)

class	Title(Elem):
	def	__init__(self, content = None, attr = {}, indent = ''):
		super().__init__('title', attr, content, 'double', indent=indent)

class	Meta(Elem):
	def	__init__(self, attr = {}, indent = ''):
		super().__init__('meta', attr, None, 'simple', indent=indent)

class	Img(Elem):
	def	__init__(self, attr = {}, indent = ''):
		super().__init__('img', attr, None, 'simple', indent=indent)

class	Table(Elem):
	def	__init__(self, content = None, attr = {}, indent = ''):
		super().__init__('table', attr, content, 'double', indent=indent)

class	Th(Elem):
	def	__init__(self, content = None, attr = {}, indent = ''):
		super().__init__('th', attr, content, 'double', indent=indent)

class	Tr(Elem):
	def	__init__(self, content = None, attr = {}, indent = ''):
		super().__init__('tr', attr, content, 'double', indent=indent)

class	Td(Elem):
	def	__init__(self, content = None, attr = {}, indent = ''):
		super().__init__('td', attr, content, 'double', indent=indent)

class	Ul(Elem):
	def	__init__(self, content = None, attr = {}, indent = ''):
		super().__init__('ul', attr, content, 'double', indent=indent)

class	Ol(Elem):
	def	__init__(self, content = None, attr = {}, indent = ''):
		super().__init__('ol', attr, content, 'double', indent=indent)

class	Li(Elem):
	def	__init__(self, content = None, attr = {}, indent = ''):
		super().__init__('li', attr, content, 'double', indent=indent)

class	H1(Elem):
	def	__init__(self, content = None, attr = {}, indent = ''):
		super().__init__('h1', attr, content, 'double', indent=indent)

class	H2(Elem):
	def	__init__(self, content = None, attr = {}, indent = ''):
		super().__init__('h2', attr, content, 'double', indent=indent)

class	P(Elem):
	def	__init__(self, content = None, attr = {}, indent = ''):
		super().__init__('p', attr, content, 'double', indent=indent)

class	Div(Elem):
	def	__init__(self, content = None, attr = {}, indent = ''):
		super().__init__('div', attr, content, 'double', indent=indent)

class	Span(Elem):
	def	__init__(self, content = None, attr = {}, indent = ''):
		super().__init__('span', attr, content, 'double', indent=indent)

class	Hr(Elem):
	def	__init__(self, attr = {}, indent = ''):
		super().__init__('hr', attr, None, 'simple', indent=indent)

class	Br(Elem):
	def	__init__(self, attr = {}, indent = ''):
		super().__init__('br', attr, None, 'simple', indent=indent)

def	cv_test():
	result = """<html lang="en">
  <head>
    <title>
      A transcended CV
    </title>
    <meta charset="UTF-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  </head>
  <body>
    <h1>
      Tanguy BOURDEAU
    </h1>
    <table>
      <th colspan="2">
        Career Path
      </th>
      <tr>
        <th>
          Years
        </th>
        <th>
          42 Cursus
        </th>
      </tr>
      <tr>
        <td>
          2022
        </td>
        <td>
          Piscine
        </td>
      </tr>
      <tr>
        <td>
          2023
        </td>
        <td>
          Minishell
        </td>
      </tr>
      <tr>
        <td>
          2024
        </td>
        <td>
          Transcendance
        </td>
      </tr>
      <tr>
        <td>
          2025
        </td>
        <td style="background-color: #424242;">
          Internship
        </td>
      </tr>
    </table>
    <h2>
      Skills
    </h2>
    <ul>
      <li>
        Management
      </li>
      <li>
        Sense of commitment
      </li>
      <li>
        Logic
      </li>
      <li>
        Persistent
      </li>
      <li>
        Passionate
      </li>
    </ul>
    <h2>
      Hobbies
    </h2>
    <ol>
      <li>
        Sport
      </li>
      <ul>
        <li>
          Snowboard
        </li>
        <li>
          Bodybuilding
        </li>
        <li>
          Swimming
        </li>
        <li>
          Crossfit
        </li>
        <li>
          Tennis
        </li>
        <li>
          Climbing
        </li>
      </ul>
      <li>
        Scoutism
      </li>
      <li>
        Coding
      </li>
      <ul>
        <li>
          Python
        </li>
        <li>
          C
        </li>
        <li>
          C++
        </li>
        <li>
          JavaScript
        </li>
        <li>
          TypeScript
        </li>
        <li>
          HTML
        </li>
        <li>
          CSS
        </li>
      </ul>
      <li>
        Video Games
      </li>
      <ul>
        <li>
          League of Legends
        </li>
        <li>
          Super Smash Bros Ultimate
        </li>
        <li>
          Teamfight Tactics
        </li>
      </ul>
    </ol>
  </body>
</html>"""

	headers = [
		Title(Text("A transcended CV")),
		Meta({'charset': "UTF-8"}),
		Meta({'name' : 'viewport', 'content': "width=device-width, initial-scale=1.0"})
	]
	head = Head(headers)
	
	table_headers = [Th(Text("Career Path"), {'colspan': "2"}), Tr([Th(Text("Years")), Th(Text("42 Cursus"))])]
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
	if str(Html([head, body], {'lang':"en"})) == result:
		print("cv_test: OK !")
	else:
		print("cv_test: KO !")

def	mandatory_test():
	result = """<html>
  <head>
    <title>
      "Hello ground!"
    </title>
  </head>
  <body>
    <h1>
      "Oh no, not again!"
    </h1>
    <img src="http://i.imgur.com/pfp3T.jpg"/>
  </body>
</html>"""
	head = Head(Title(Text("\"Hello ground!\"")))
	body = Body([H1(Text("\"Oh no, not again!\"")), Img({'src': "http://i.imgur.com/pfp3T.jpg"})])
	if (str(Html([head, body]))) == result:
		print("mandatory_test: OK !")
	else:
		print("mandatory_test: KO !")
	print(str(Html([head, body])))

def	complementary_test():
	result = """<p>
  <div>
    <hr/>
    <br/>
    <span>
      last test
    </span>
  </div>
</p>"""
	if (str(P(Div([Hr(), Br(), Span(Text("last test"))])))) == result:
		print("complementary_test: OK !")
	else:
		print("complementary_test: KO !")

if __name__ == '__main__':
	try :
		cv_test()
		complementary_test()
		mandatory_test()
	except Exception as e:
		print(e)
