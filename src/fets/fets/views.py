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
        'my': random_user(),
    }
    return render(request, 'itemDetails.html', content)

def evaluate(request, type_):
    content = {
        'title': type_,
        'subtype': {
            'name': random_word(),
            "highestPrice": random.randint(10000, 99999),
            'history': random.randint(1000, 9999),
        },
        'options': [random_option() for _ in range(6)],
    }
    return render(request, 'evaluate.html', content)

def evaluateMenu(request):
    content = {
        'title': '估价选单',
        'subtypes': [
            [{'name': random_word(), 'logo': "apple.png", 'href': random_word()} for _ in range(20)] for _ in range(4)
        ],
    }
    return render(request, 'evaluateMenu.html', content)