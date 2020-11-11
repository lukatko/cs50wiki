from django.shortcuts import render
import markdown2
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
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
