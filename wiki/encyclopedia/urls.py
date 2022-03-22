from unicodedata import name
from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:TITLE>", views.title, name='TITLE'),
    path("/search", views.search_entry, name="search"),
    path("/create", views.create_new, name="create")
]
