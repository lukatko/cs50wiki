from django.shortcuts import render

import utl


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": utl.list_entries()
    })

