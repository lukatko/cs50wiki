from django.shortcuts import render, redirect, HttpResponse
import markdown2
from . import util
from . import forms
import random

def search(request):
    if (request.method == "POST"):
        form = forms.SearchForm(request.POST)
        if (form.is_valid()):
            value = form.cleaned_data["search"]
            entries = util.list_entries()
            if (value in entries):
                return redirect(f"/wiki/{value}")
            else:
                strings_with_value = [i for i in entries if value in i]
                return render(request, "encyclopedia/search.html", {
                    "entries": strings_with_value,
                    "search": value,
                    "form": forms.SearchForm()
                })
    else:
        return index(request)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": forms.SearchForm()
    })

def entry(request, entry):
    if (request.method == "POST"):
        return edit_page(request, entry)
    else:
        argument = util.get_entry(entry)
        if (argument is None):
            return render(request, "encyclopedia/error.html", {
                "entry": entry,
                "form": forms.SearchForm()
            })
        else:
            return render(request, "encyclopedia/entry.html", {
                "name": entry,
                "entry": markdown2.markdown(argument),
                "form": forms.SearchForm()
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
                    "form": forms.SearchForm,
                    "create_form": forms.CreateForm(),
                    "flag": 1
                })
            else:
                util.save_entry(title, text)
                return redirect(f"wiki/{title}")
    else:
        return render(request, "encyclopedia/create.html", {
            "form": forms.SearchForm(),
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
            "form": forms.SearchForm(),
            "edit_form": form
        })

def random_page(request):
    return redirect(f'/wiki/{random.choice(util.list_entries())}')      
