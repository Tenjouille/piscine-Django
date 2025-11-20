from django.urls import path
from . import views

urlpatterns = [
	path("", views.shadedTab, name='shaded_tab')
]