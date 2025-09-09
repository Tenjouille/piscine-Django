import sys
import os
import re

def	parse_settings():
	var = {}
	with open("/home/tbourdea/Piscine-Django/Day02/ex00/settings.py", 'r') as f:
		vars = f.read()
	exec(vars, {}, var)
	return var

def	handle_dict(elem, val, indent):
	res = f"{indent}<li>\n{indent}\t{replace_in_html(elem, indent)}\n"
	new_indent = indent + '\t'
	if val[elem] == None:
		return res + indent + "</li>\n"
	if type(val[elem]) != list and type(val[elem]) != dict:
		return res + f"{new_indent}<li>{replace_in_html(val[elem], new_indent)}</li>\n"
	return res + replace_in_html(val[elem], new_indent) + indent + "</li>\n"


def	handle_list(elem, new_indent):
	if type(elem) != list and type(elem) != dict:
		return f"{new_indent}<li>{replace_in_html(elem, new_indent)}</li>\n"
	else:
		return replace_in_html(elem, new_indent)

def	replace_in_html(val, indent):
	res = ""
	ol = ""
	ul = ""
	li = ""
	if type(val) == list or type(val) == dict:
		if type(val) == list:
			ol = "<ol>"
		elif type(val) == dict:
			ul = "<ul>"
		res += indent + ol + ul + "\n"
		new_indent = indent + '\t'
		for elem in val:
			if type(val) == list:
				res += handle_list(elem, new_indent)
			elif type(val) == dict:
				res += handle_dict(elem, val, new_indent)
		if type(val) == list:
			res += f"{indent}</ol>\n"
		elif type(val) == dict:
			res += f"{indent}</ul>\n"
	else:
		res += val
	return res

def	parse_template(data: dict):
	html = ""
	var = ""
	if sys.argv[1].split('.')[-1] != "template":
		raise Exception("Error : Le fichier modèle doit avoir l'extension \'.template\'")
	with open(sys.argv[1]) as f:
		while True:
			chunk = f.read(1)
			if chunk == '':
				break
			if chunk == '{':
				while chunk != '}':
					chunk = f.read(1)
					if chunk == '' or chunk == '{':
						raise Exception(f"Error: {sys.argv[1]} contient des accolades non fermées")
					if chunk != '}':
						var += chunk
				if var in data.keys():
					if type(data[var]) == list or type(data[var]) == dict:
						html += f"\t<h3>{var.title()}</h3>\n"
					html += replace_in_html(data[var], '\t')
					var = ""
				else:
					raise Exception(f"Error: {sys.argv[1]} contient des élements entre accolades n'existant pas dans le fichier settings.py : {var}")
			else:
				html += chunk
	return (html)

if __name__ == "__main__":
	if (len(sys.argv) == 2):
		try:
			data = parse_settings()
			html = parse_template(data)
			with open(sys.argv[1].split('.template')[0] + '.html', 'w') as f:
				f.write(html)
		except Exception as e:
			print(str(e))