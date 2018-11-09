# -*- coding: utf-8 -*-  
from django.db import models
from django.contrib.auth.hashers import make_password, check_password
# Create your models here.

class Follower(models.Model):
    Follower=models.BigIntegerField()
    Following=models.BigIntegerField()

class User(models.Model):        
        
    UserId=models.AutoField(primary_key=True)
    UserType=models.IntegerField(default=1)
    Nickname=models.CharField(max_length=50)
    Icon=models.ImageField()
    Photo=models.ImageField()
    Email=models.CharField(max_length=50)
    PhoneNumber=models.IntegerField(default=0)
    Password=models.CharField(max_length=254)
    isIdentified=models.BooleanField(default=False)
    isVIP=models.BooleanField(default=False)
    CreatedAt=models.DateTimeField(auto_now_add=True)
    UpdateAt=models.DateTimeField(auto_now=True)

    def Create_User(self,Email,Password,Nickname="John Doe"):
        UserType=1

        psw=make_password(Password)
        new_user=User(UserType=UserType,Nickname=Nickname,Email=Email,Password=psw)

        user_list=User.objects.filter(Email=Email)
        if(len(user_list)!=0):  return "Email same"
        else:   
            new_user.save()
            return new_user.UserId

    def Login(self,Email,Password):
        user_list=User.objects.filter(Email=Email)
        if(len(user_list)!=1):  return "user does not exist"
        if(check_password(Password,user_list[0].Password)): return True
        else:   return "wrong password"

    def __str__(self):
        return self.UserId+self.UserType+self.Nickname

class AppendInfos(models.Model):
    #UserId=models.ForeignKey(User,on_delete=models.CASCADE)
    UserId=models.AutoField(primary_key=True)
    MoyuCoin=models.IntegerField(default=0)

class Buyer(models.Model):
    #UserId=models.ForeignKey(User,on_delete=models.CASCADE)
    UserId=models.AutoField(primary_key=True)
    DeliveryState=models.CharField(max_length=50)

class Seller(models.Model):
    #UserId=models.ForeignKey(User,on_delete=models.CASCADE)
    UserId=models.AutoField(primary_key=True)
    Credit=models.CharField(max_length=50)
    Star=models.IntegerField(default=0)

class Item(models.Model):
    ItemId=models.AutoField(primary_key=True)
    #UserId=models.ForeignKey(User,on_delete=models.CASCADE)
    UserId=models.BigIntegerField()
    Name=models.CharField(max_length=50)
    Price=models.CharField(max_length=50)
    Description=models.TextField(max_length=65535)
    isForRent=models.BooleanField(default=False)
    ShortCut=models.CharField(max_length=50)
    Datetime=models.DateTimeField(auto_now_add=True)
    Place=models.CharField(max_length=50)
    BaoYou=models.BooleanField(default=False)
    Negotiation=models.BooleanField(default=False)
    Classification=models.CharField(max_length=50)
    AppendInfoId=models.CharField(max_length=50)
    VisitNum=models.IntegerField(default=0)
    XinJiu=models.CharField(max_length=50)

    def Create_Item(self,UserId,Name):
        user_list=User.objects.filter(UserId=UserId)
        if(len(user_list)!=1):   return "cannot find user"
        new_item=Item(UserId=UserId,Name=Name)
        new_item.save()
        return new_item.ItemId

class Order(models.Model):
    OrderId=models.AutoField(primary_key=True)
    BuyerId=models.BigIntegerField()
    SellerId=models.BigIntegerField()
    #ItemId=models.ForeignKey(Item,on_delete=models.CASCADE,)
    ItemId=models.BigIntegerField()
    CreatedAt=models.DateTimeField(auto_now_add=True)
    Address=models.CharField(max_length=254,default='')
    DeliveryState=models.CharField(max_length=50)

    def Create_Order(self,BuyerId,SellerId,ItemId,Address,DeliveryState="未发货"):
        buyer_list=User.objects.filter(UserId=BuyerId)
        if(len(buyer_list)!=1):   return "cannot find buyer"
        seller_list=User.objects.filter(UserId=SellerId)
        if(len(seller_list)!=1):   return "cannot find seller"
        item_list=Item.objects.filter(ItemId=ItemId)
        if(len(item_list)!=1):   return "cannot find item"

        new_order=Order(BuyerId=BuyerId,SellerId=SellerId,ItemId=ItemId,Address=Address,DeliveryState=DeliveryState)
        new_order.save()
        return new_order.OrderId


class Comment(models.Model):
    CommentId=models.AutoField(primary_key=True)
    #ItemId=models.ForeignKey(Item,on_delete=models.CASCADE,)
    ItemId=models.BigIntegerField()
    #UserId=models.ForeignKey(User,on_delete=models.CASCADE,)
    UserId=models.BigIntegerField()
    Text=models.TextField(max_length=65535)
    Datetime=models.DateTimeField(auto_now_add=True)
    SubCommentId=models.BigIntegerField(default=None)

    def Create_Comment(self,ItemId,UserId,Text="",SubCommentId=-1):
        user_list=User.objects.filter(UserId=UserId)
        if(len(user_list)!=1):   return "cannot find user"
        item_list=Item.objects.filter(ItemId=ItemId)
        if(len(item_list)!=1):   return "cannot find item"
        if(SubCommentId!=-1):
            Comment_list=Comment.objects.filter(CommentId=SubCommentId)
            if(len(Comment_list)!=1):   return "cannot find comment"
        new_comment=Comment(ItemId=ItemId,UserId=UserId,Text=Text,SubCommentId=SubCommentId)
        new_comment.save()
        return new_comment.CommentId

    def __str__(self):
        return "Item:"+self.ItemId+":"+"User:"+self.UserId+":"+self.Datetime

class Reward(models.Model):
    RewardId=models.AutoField(primary_key=True)
    #UserId=models.ForeignKey(Buyer,on_delete=models.CASCADE,)
    UserId=models.BigIntegerField()
    Name=models.CharField(max_length=50)
    Description=models.TextField(max_length=65535)
    Price=models.IntegerField(default=0)
    #Negotiation=models.BooleanField
    CreatedAt=models.DateTimeField(auto_now_add=True)
    Place=models.CharField(max_length=50)

    def Create_Reward(self,UserId,Name="default_name",Description="",Price=0,Place=""):
        user_list=User.objects.filter(UserId=UserId)
        if(len(user_list)!=1):   return "cannot find user"
        new_reward=Reward(UserId=UserId,Name=Name,Description=Description,Price=Price,Place=Place)
        new_reward.save()
        return new_reward.RewardId

