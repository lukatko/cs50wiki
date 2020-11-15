from django.shortcuts import render, redirect, HttpResponse
import markdown2
from . import util
from . import forms
import random

def search(request):
    if (request.method == "GET"):
        search = request.GET.get("search")
        if (search in util.list_entries()):
            return redirect(f"/wiki/{search}")
        else:
            posts = [i for i in util.list_entries() if search in i]
            return render(request, "encyclopedia/search.html", {
                "search": search,
                "entries": posts
            })


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    if (request.method == "POST"):
        return edit_page(request, entry)
    else:
        argument = util.get_entry(entry)
        if (argument is None):
            return render(request, "encyclopedia/error.html", {
                "entry": entry
            })
        else:
            return render(request, "encyclopedia/entry.html", {
                "name": entry,
                "entry": markdown2.markdown(argument)
            })

def create_new_page(request):
    if (request.method == "POST"):
        form  = forms.CreateForm(request.POST)
        if (form.is_valid()):
            text = form.cleaned_data["create"]
            title = form.cleaned_data["title"]
            if (title in util.list_entries()):
                util.save_entry(title, text)
                return render(request, "encyclopedia/create.html", {
                    "create_form": forms.CreateForm(),
                    "flag": 1
                })
            else:
                util.save_entry(title, text)
                return redirect(f"wiki/{title}")
    else:
        return render(request, "encyclopedia/create.html", {
            "create_form": forms.CreateForm(),
            "flag": 0
        })

def edit_page(request, entry):
    if (request.method == "POST"):
        form = forms.EditForm(request.POST)
        if (form.is_valid()):
            content = form.cleaned_data["edit"]
            util.save_entry(entry, content)
            return redirect(f'/wiki/{entry}')
    else:
        form = forms.EditForm({'edit': util.get_entry(entry)})
        return render(request, 'encyclopedia/edit.html', {
            "entry": entry,
            "edit_form": form
        })

def random_page(request):
    return redirect(f'/wiki/{random.choice(util.list_entries())}')      
