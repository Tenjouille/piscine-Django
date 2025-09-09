import sys

def	parsing_elem(params : list[str]):
	res : dict[str, str] = {}
	split_params = [param.split(':') for param in params]
	if len(split_params) != 5:
		raise Exception(f"Error: {sys.argv[1]} is not in a  good format")

	if split_params[0][0] == 'position':
		res.update({split_params[0][0]: split_params[0][1]})
	if split_params[1][0] == 'number':
		res.update({split_params[1][0]: split_params[1][1]})
	if split_params[2][0] == 'small':
		res.update({split_params[2][0]: split_params[2][1]})
	if split_params[3][0] == 'molar':
		res.update({split_params[3][0]: split_params[3][1]})

	if split_params[4][0] != 'electron' or len(res) != 4:
		raise Exception(f"Error: {sys.argv[1]} is not in a good format")
	return res

def	parsing_file():
	if len(sys.argv) != 2:
		raise Exception(f"Error: you need to enter one unique argument, which has to be the path to the file containing a correct elements data format")
	with open(sys.argv[1]) as file:
		rows = file.read().split('\n')
	data : dict[str, dict[str, str]] = {}
	for row in rows:
		if row != '':
			data.update({row.split(' = ')[0] : parsing_elem(row.split(' = ')[1].split(', '))})
	return data

def	generate_header():
	return '''<head>
\t<meta charset='utf-8'>
\t<meta http-equiv='X-UA-Compatible' content='IE=edge'>
\t<title>Page Title</title>
\t<meta name='viewport' content='width=device-width, initial-scale=1'>
\t<link rel='stylesheet' type='text/css' media='screen' href='main.css'>
\t<script src='main.js'></script>
</head>
'''

def	generate_body(data: dict):
	body : str = "<body>\n\t<table>\n"
	indent: int = '\t\t\t'
	position: int = 0
	
	for perio_elem_name in data:
		if data[perio_elem_name]['position'] == '0':
			body += "\t\t<tr>\n"
		while data[perio_elem_name]['position'] != str(position):
			body += indent + "<td></td>\n"
			position += 1
			if position == 18:
				position = 0
		body += indent + "<td style=\"border: 1px solid black;\">\n"
		body += indent + f"\t<h4 style=\"text-align: center;\">{perio_elem_name}</h4>\n"
		body += indent + f"\t<ul>\n{indent}\t\t<li>Nº{data[perio_elem_name]['number']}</li>\n"
		body += indent + f"\t\t<li>{data[perio_elem_name]['small']}</li>\n"
		body += indent + f"\t\t<li>{data[perio_elem_name]['molar']}</li>\n"
		body += indent + f"\t</ul>\n{indent}</td>\n"
		if data[perio_elem_name]['position'] == '17':
			body += "\t\t</tr>\n"
		position += 1
		if position == 18:
			position = 0
	body += "\t</table>\n</body>\n"
	return body

def	periodic_table():
	try:
		data : dict[str, dict[str, str]] = parsing_file()
	except Exception as e:
		print(str(e))
		return
	header : str = generate_header()
	body : str = generate_body(data)
	html_page : str = "<!DOCTYPE html>\n<html>\n"
	html_page += header + body
	html_page += "</html>"
	with open("periodic_table.html", 'w') as f:
		f.write(html_page)

if __name__ == "__main__":
	periodic_table()