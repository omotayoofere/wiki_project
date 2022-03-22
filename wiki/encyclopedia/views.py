from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from . import forms

from . import util
from re import search


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

#def title(entry):
#    return util.get_entry(entry)
def title(request, TITLE):
    for a in util.list_entries():
        if a == TITLE:
            return render(request, "encyclopedia/entry.html", {"entry": util.get_entry(TITLE)})

def search_entry(request):
    
    if request.method == "GET":
        entry = request.GET.get('q').lower()
        entries = util.list_entries()
        
        store = []
    
        if entry in map(str.lower, entries):
            #return HttpResponseRedirect(f"encyclopedia/{entry}")
            return render(request, "encyclopedia/entry.html", {
                "entry": util.get_entry(entry)})

        for x in map(str.lower, entries):
            if entry in x:
                store.append(x)
            else:
                pass

        if store:
            return render(request, "encyclopedia/search_results.html", {
                "entry": store})
#       elif entry.lower() in a for x in a:
#                store.append(entry)
#                return render(request, "encyclopedia/search_results.html", {"entry": store})

        else:
            return render(request, "encyclopedia/404.html")

def create_new(request):
    if request.method == "POST":
        form = forms.NewEntryForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

            if title in util.list_entries():
                return HttpResponse("Entry exists")
            else:
                util.save_entry(title, content)
                return HttpResponseRedirect(reverse("encyclopedia:index"))
        else:
            return render(request, "encyclopedia/create.html",{
                "form":form
            })

    else:
        return render(request, "encyclopedia/create.html",{
                "form":forms.NewEntryForm()
            })
