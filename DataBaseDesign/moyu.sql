/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2018/10/6 13:41:14                           */
/*==============================================================*/


drop table if exists AppendInfos;

drop table if exists Buyers;

drop table if exists Comments;

drop table if exists Items;

drop table if exists Orders;

drop table if exists Rewards;

drop table if exists Sellers;

drop table if exists Users;

/*==============================================================*/
/* Table: AppendInfos                                           */
/*==============================================================*/
create table AppendInfos
(
   AppendInfoId         varchar(50) not null,
   UserId               varchar(50) not null,
   MoyuCoin             int,
   Follower             int,
   Following            int,
   Star                 int,
   primary key (AppendInfoId)
);

/*==============================================================*/
/* Table: Buyers                                                */
/*==============================================================*/
create table Buyers
(
   BuyerId              varchar(50) not null,
   UserId               varchar(50) not null,
   DeliveryAddress      varchar(50),
   primary key (BuyerId)
);


/*==============================================================*/
/* Table: Comments                                              */
/*==============================================================*/
create table Comments
(
   CommentId            varchar(50) not null,
   ItemId               varchar(50) not null,
   UserId               varchar(50) not null,
   Comment              varchar(65535) not null,
   DateTime             datetime not null,
   SubCommentId         varchar(50),
   primary key (CommentId)
);


/*==============================================================*/
/* Table: Items                                                 */
/*==============================================================*/
create table Items
(
   ItemId               varchar(50) not null,
   SellerId             varchar(50) not null,
   Name                 varchar(50) not null,
   Price                varchar(50) not null,
   Description          varchar(65535),
   IsForRent            bool,
   ShortCut             varchar(50),
   DateTime             datetime not null,
   Place                varchar(50) not null,
   BaoYou               bool,
   Negotiation          bool,
   Classification       varchar(50),
   AppendInfoId         varchar(50),
   primary key (ItemId)
);


/*==============================================================*/
/* Table: Orders                                                */
/*==============================================================*/
create table Orders
(
   OrderId              varchar(50) not null,
   BuyerId              varchar(50) not null,
   SellerId             varchar(50) not null,
   ItemId               varchar(50) not null,
   CreatedAt            timestamp,
   DeliveryState        varchar(50) not null,
   primary key (OrderId)
);

/*==============================================================*/
/* Table: Rewards                                               */
/*==============================================================*/
create table Rewards
(
   RewardId             varchar(50) not null,
   BuyerId              varchar(50) not null,
   Name                 varchar(50) not null,
   Description          varchar(65535),
   Price                int not null,
   Negotiation          bool,
   CreatedAt            timestamp not null,
   Place                varchar(50) not null,
   primary key (RewardId)
);


/*==============================================================*/
/* Table: Sellers                                               */
/*==============================================================*/
create table Sellers
(
   SellerId             varchar(50) not null,
   UserId               varchar(50) not null,
   Credit               varchar(50),
   primary key (SellerId)
);


/*==============================================================*/
/* Table: Users                                                 */
/*==============================================================*/
create table Users
(
   UserId               varchar(50) not null,
   UserType             int not null,
   Nickname             varchar(50),
   Icon                 varchar(65535),
   Photo                varchar(65535),
   Email                varchar(50),
   PhoneNumber          decimal(11,0) not null,
   Password             varchar(50) not null,
   BuyerId              varchar(50),
   SellerId             varchar(50),
   IsIdentiyied         bool,
   IsVIP                bool,
   CreatedAt            timestamp,
   UpdatedAt            timestamp,
   AppendInfoId         varchar(50),
   primary key (UserId)
);

/*==============================================================*/
/* Tests                                               			*/
/*==============================================================*/
insert into Users (UserId, UserType, Nickname, PhoneNumber, Password) values('0','0','Admin', '10000000000', 'password');
insert into Users (UserId, UserType, Nickname, PhoneNumber, Password) values('1','1','User1', '10000000001', 'password');
insert into Users (UserId, UserType, Nickname, PhoneNumber, Password) values('2','1','User2', '10000000002', 'password');

insert into Buyers (BuyerId, UserId, DeliveryAddress) values('1','1','上海');
insert into Sellers (SellerId, UserId, Credit) values('2','2','good/100');

insert into Items (ItemId, SellerId, Name, Price, DateTime, Place) values('0', '2', 'Item1', '3.33$', '2018-10-1 0:0:0', '上海');

insert into Orders (OrderId, BuyerId, SellerId, ItemId, DeliveryState) values('0','1', '2', '0', 'on delivery');

