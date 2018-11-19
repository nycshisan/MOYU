class User:
    def __init__(self, id, name, avatar, location, contact):
        self.id = id
        self.name = name
        self.avatar = '/static/imgs/' + avatar
        self.location = location
        self.contact = contact

class ItemInfo:
    def __init__(self, name, pics, desc, price, pubtime):
        self.name = name
        self.pics = list(map(lambda name: '/static/imgs/' + name, pics))
        self.desc = desc
        self.price = price
        self.pubtime = pubtime

class ItemDetails:
    def __init__(self, original_price, condition, visit_number, update_time):
        self.original_price = original_price
        self.condition = condition
        self.visit_number = visit_number
        self.update_time = update_time

class Item:
    def __init__(self, seller, info, details, href, comments):
        self.seller = seller
        self.info = info
        self.details = details
        self.href = '/itemDetails/' + href
        self.comments = comments

class ItemCommentElement:
    def __init__(self, user, content, time):
        self.user = user
        self.content = content
        self.time = time

class ItemComment:
    def __init__(self, ele, subcomments=[]):
        self.ele = ele
        self.subcomments = subcomments
        self.is_toplevel = self.subcomments == []
