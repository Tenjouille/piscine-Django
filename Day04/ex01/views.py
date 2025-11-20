from django.shortcuts import render
from django.template import loader

def	django(request):
	context = {
		'nav_list' : [
			'affichage',
			'templates'
		]
	}
	return render(request, "ex01/django.html", context=context)

def	affichage(request):
	context = {
		'nav_list' : [
			'django',
			'templates'
		]
	}
	return render(request, "ex01/affichage.html", context=context)

def	templates(request):
	context = {
		'nav_list' : [
			'django',
			'affichage'
		]
	}
	return render(request, "ex01/templates.html", context=context)