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
    details = random_itemdetail()
    href = random_word()
    return Item(seller, info, details, href)

def random_user():
    name = random_word()
    avatar = 'DefaultAvatar.jpg'
    location = random_word()
    contact = ''.join([str(random.randint(0, 9)) for _ in range(11)])
    return User(name, avatar, location, contact)

def random_iteminfo():
    name = random_word()
    pics = ['DefaultItemPic{}.jpg'.format(random.randint(1, 10)) for _ in range(random.randint(1, 5))]
    desc = random_paragraph(5, 30)
    price = random.randint(1, 10000)
    pubtime = random_interval_string()
    return ItemInfo(name, pics, desc, price, pubtime)

def random_itemdetail():
    original_price = random.randint(1, 10000)
    condition = str(random.randint(1, 99)) + '%'
    visit_number = random.randint(1, 10000)
    update_time = random.randint(1, 10000)
    return ItemDetails(original_price, condition, visit_number, update_time)