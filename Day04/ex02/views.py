from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MyForm
from pathlib import Path
from datetime import datetime

import logging


# Récupère les entrées du fichier de log, tout en laissant de côté les infos d'horodatage.
def	updateHistory() -> list[str]:
	ret = []
	with open("ex02/form.log", 'a+') as f:
		f.seek(0)
		for line in f.read().split('\n'):
			if not line:
				continue
			date, _, value = line.partition('->')
			date = date.strip('[] ')
			dt = datetime.strptime(date, "%Y-%m-%d %H:%M:%S,%f")
			ret.append({'date': dt.strftime("%d.%m.%Y at %Hh%Mmin %Ssec"), 'value': value})
	return ret


def	form(request):
	logger = logging.getLogger(__name__)
	history = updateHistory()
	if request.method == "POST":
		form = MyForm(request.POST)
		if form.is_valid():
			logger.info(form.cleaned_data['input'])
			return redirect('form')
	else:
		form = MyForm()

	history = updateHistory()
	return render(request, "ex02/my_form.html", {"form": form, "history": history})
