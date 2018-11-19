from django.shortcuts import render

from fets.misc import *

def login(request):
    return render(request, "login.html", {'title': 'login'})

def register(request):
    return render(request, "register.html", {'title': 'register'})

def catalog(request, catalog):
    content = {
        'title': catalog,
        'catalogs': random_words(5),
        'subtypes': random_words(20),
        'items': [random_item() for _ in range(50)],
    }
    return render(request, 'items.html', content)

def item(request, item):
    content = {
        'title': item,
        'item': random_item(),
    }
    return render(request, 'itemDetails.html', content)
