from django.shortcuts import render

from . import util

from .util import get_entry


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry (request, entry):
    
    entry = get_entry(entry)
    if entry:
        return render(request, "encyclopedia/entries.html",{"entry": entry})
    else:
        return render(request, "encyclopedia/entry_not_found.html")