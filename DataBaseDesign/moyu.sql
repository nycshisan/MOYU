/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2018/10/19 10:16:39                          */
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
   UserId               varchar(50) not null,
   MoyuCoin             int,
   Follower             int,
   Following            int,
   Star                 int,
   primary key (UserId)
);

/*==============================================================*/
/* Table: Buyers                                                */
/*==============================================================*/
create table Buyers
(
   UserId               varchar(50) not null,
   DeliveryAddress      varchar(50),
   primary key (UserId)
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
   Sel_UserId           varchar(50) not null,
   ChengSe              varchar(50),
   Title                varchar(50) not null,
   Price                numeric(50,2) not null,
   Description          varchar(65535),
   IsForRent            bool,
   ShortCut             longblob,
   DateTime             datetime,
   Place                varchar(50),
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
   ItemId               varchar(50) not null,
   Buy_UserId           varchar(50),
   Sel_UserId           varchar(50),
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
   Buy_UserId           varchar(50),
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
   UserId               varchar(50) not null,
   Credit               varchar(50),
   star                 int,
   primary key (UserId)
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
   IsIdentiyied         bool,
   IsVIP                bool,
   CreatedAt            timestamp,
   UpdatedAt            timestamp,
   primary key (UserId)
);

/*==============================================================
alter table AppendInfos add constraint FK_Reference_7 foreign key (UserId)
      references Users (UserId) on delete restrict on update restrict;

alter table Buyers add constraint FK_Reference_5 foreign key (UserId)
      references Users (UserId) on delete restrict on update restrict;

alter table Comments add constraint FK_Reference_13 foreign key (ItemId)
      references Items (ItemId) on delete restrict on update restrict;

alter table Comments add constraint FK_Reference_14 foreign key (UserId)
      references Users (UserId) on delete restrict on update restrict;

alter table Items add constraint FK_Reference_11 foreign key (Sel_UserId)
      references Sellers (UserId) on delete restrict on update restrict;

alter table Orders add constraint FK_Reference_10 foreign key (Buy_UserId)
      references Buyers (UserId) on delete restrict on update restrict;

alter table Orders add constraint FK_Reference_8 foreign key (ItemId)
      references Items (ItemId) on delete restrict on update restrict;

alter table Orders add constraint FK_Reference_9 foreign key (Sel_UserId)
      references Sellers (UserId) on delete restrict on update restrict;

alter table Rewards add constraint FK_Reference_12 foreign key (Buy_UserId)
      references Buyers (UserId) on delete restrict on update restrict;

alter table Sellers add constraint FK_Reference_6 foreign key (UserId)
      references Users (UserId) on delete restrict on update restrict;                                           			*/
/*==============================================================*/


/*==============================================================*/
/* Tests                                               			*/
/*==============================================================*/
insert into Users (UserId, UserType, Nickname, PhoneNumber, Password) values('0','0','Admin', '10000000000', 'password');
insert into Users (UserId, UserType, Nickname, PhoneNumber, Password) values('1','1','User1', '10000000001', 'password');
insert into Users (UserId, UserType, Nickname, PhoneNumber, Password) values('2','1','User2', '10000000002', 'password');

insert into Buyers (UserId, DeliveryAddress) values('1','上海');
insert into Sellers (UserId, Credit) values('2','good/100');

insert into Items (ItemId, Sel_UserId, Title, Price, DateTime, Place) values('0', '2', 'Item1', '3.33$', '2018-10-1 0:0:0', '上海');

insert into Orders (OrderId, Buy_UserId, Sel_UserId, ItemId, DeliveryState) values('0','1', '2', '0', 'on delivery');