class User:
    def __init__(self, name, avatar, location):
        self.name = name
        self.avatar = '/static/imgs/' + avatar
        self.location = location

class ItemInfo:
    def __init__(self, name, pic, desc, price, pubtime):
        self.name = name
        self.pic = '/static/imgs/' + pic
        self.desc = desc
        self.price = price
        self.pubtime = pubtime

class Item:
    def __init__(self, seller, info, comments=[]):
        self.seller = seller
        self.info = info
        self.comments = comments