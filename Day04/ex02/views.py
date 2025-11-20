from django.shortcuts import render
from django.http import HttpResponse
from .forms import MyForm
from pathlib import Path

import logging

# Récupère les entrées du fichier de log, tout en laissant de côté les infos d'horodatage.
def	updateHistory() -> list[str]:
	ret = []
	with open("ex02/form.log", 'a+') as f:
		f.seek(0)
		return ['-> '.join(line.split('-> ')[1:]) for line in f.read().split('\n')]


def	form(request):
	logger = logging.getLogger(__name__)
	history = updateHistory()
	if request.method == "POST":
		form = MyForm(request.POST)
		if form.is_valid():
			logger.info(form.cleaned_data['input'])
			history.append(form.cleaned_data['input'])
			return render(request, "ex02/my_form.html", {"form": form, "history": history})
	else:
		form = MyForm()

	return render(request, "ex02/my_form.html", {"form": form})