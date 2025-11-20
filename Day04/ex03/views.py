from django.shortcuts import render

def	shadedTab(request):
	rgb_scope = []
	for i in range(50):
		rgb_scope.append({
			"noir": f"rgb({i * 2}%, {i * 2}%, {i * 2}%)",
			"rouge": f"rgb(100%, {i * 2}%, {i * 2}%)",
			"bleu": f"rgb({i * 2}%, 100%, {i * 2}%)",
			"vert": f"rgb({i * 2}%, {i * 2}%, 100%)"
		})

	return render(request, "ex03/shaded_tab.html", {'rgb_scope' : rgb_scope})