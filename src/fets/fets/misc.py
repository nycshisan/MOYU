import random

from fets.types import *

word_file = "/usr/share/dict/words"
words = open(word_file).read().splitlines()

def random_word():
    return random.choice(words)

def random_words(length):
    return [random_word() for _ in range(length)]

def random_paragraph(min_length, max_length):
    l = random.randint(min_length, max_length)
    return ' '.join(random_words(l))

def random_interval_string():
    units = ['minutes', 'hours', 'days', 'months']
    unit = random.choice(units)
    number = random.randint(1, 20)
    return str(number) + ' ' + unit

def random_item():
    seller = random_user()
    info = random_iteminfo()
    return Item(seller, info)

def random_user():
    name = random_word()
    avatar = 'DefaultAvatar.jpg'
    location = random_word()
    return User(name, avatar, location)

def random_iteminfo():
    name = random_word()
    pic = 'DefaultItemPic{}.jpg'.format(random.randint(1, 10))
    desc = random_paragraph(5, 30)
    price = random.randint(1, 10000)
    pubtime = random_interval_string()
    return ItemInfo(name, pic, desc, price, pubtime)

