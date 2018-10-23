from django.db import models

# Create your models here.

class Follower(models.Model):
    Follower=models.BigIntegerField(primary_key=True)
    Following=models.BigIntegerField()   

class User(models.Model):
    UserId=models.BigIntegerField(primary_key=True)
    UserType=models.IntegerField
    Nickname=models.CharField(max_length=50)
    Icon=models.ImageField()
    Photo=models.ImageField()
    Email=models.CharField(max_length=50)
    PhoneNumber=models.IntegerField
    Password=models.CharField(max_length=50)
    isIdentified=models.BooleanField
    isVIP=models.BooleanField
    CreatedAt=models.DateTimeField(auto_now_add=True)
    UpdateAt=models.DateTimeField(auto_now=True)

class AppendInfos(models.Model):
    #UserId=models.ForeignKey(User,on_delete=models.CASCADE)
    UserId=models.BigIntegerField(primary_key=True)
    MoyuCoin=models.IntegerField

class Buyer(models.Model):
    #UserId=models.ForeignKey(User,on_delete=models.CASCADE)
    UserId=models.BigIntegerField(primary_key=True)
    DeliveryState=models.CharField(max_length=50)

class Seller(models.Model):
    #UserId=models.ForeignKey(User,on_delete=models.CASCADE)
    UserId=models.BigIntegerField(primary_key=True)
    Credit=models.CharField(max_length=50)
    Star=models.IntegerField

class Item(models.Model):
    ItemId=models.BigIntegerField(primary_key=True)
    #UserId=models.ForeignKey(User,on_delete=models.CASCADE)
    UserId=models.BigIntegerField()
    Name=models.CharField(max_length=50)
    Price=models.CharField(max_length=50)
    Description=models.TextField(max_length=65535)
    isForRent=models.BooleanField
    ShortCut=models.CharField(max_length=50)
    Datetime=models.DateTimeField(auto_now_add=True)
    Place=models.CharField(max_length=50)
    BaoYou=models.BooleanField
    Negotiation=models.BooleanField
    Classification=models.CharField(max_length=50)
    AppendInfoId=models.CharField(max_length=50)
    VisitNum=models.IntegerField(default=0)
    XinJiu=models.CharField(max_length=50)

class Order(models.Model):
    OrderId=models.BigIntegerField(primary_key=True)
    BuyerId=models.BigIntegerField()
    SellerId=models.BigIntegerField()
    #ItemId=models.ForeignKey(Item,on_delete=models.CASCADE,)
    ItemId=models.BigIntegerField()
    CreatedAt=models.DateTimeField(auto_now_add=True)
    DeliveryState=models.CharField(max_length=50)


class Comment(models.Model):
    CommentId=models.BigIntegerField(primary_key=True)
    #ItemId=models.ForeignKey(Item,on_delete=models.CASCADE,)
    ItemId=models.BigIntegerField()
    #UserId=models.ForeignKey(User,on_delete=models.CASCADE,)
    UserId=models.BigIntegerField()
    Comment=models.TextField(max_length=65535)
    Datetime=models.DateTimeField(auto_now_add=True)
    SubCommentId=models.BigIntegerField()

class Reward(models.Model):
    RewardId=models.BigIntegerField(primary_key=True)
    #UserId=models.ForeignKey(Buyer,on_delete=models.CASCADE,)
    UserId=models.BigIntegerField()
    name=models.CharField(max_length=50)
    Description=models.TextField(max_length=65535)
    Price=models.IntegerField
    #Negotiation=models.BooleanField
    CreatedAt=models.DateTimeField(auto_now_add=True)
    Place=models.CharField(max_length=50)
