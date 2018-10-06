#数据库设计补充说明
##Users table
UserType : 管理员(0)或普通用户(1)
PhoneNumber : 预计用手机号登陆(或邮箱)
BuyerId/SellerId :对应的买卖家Id，　可以与UserId相同,或不同
IsIdentified: 是(1)否(0)实名
##Items table
IsForRent: 是(1)否(0)租用
ShortCut: 一张图片或缩略图
Place: 发布地点
BaoYou: 是(1)否(0)包邮
Negotiation: 可(1)否(0)议价
Classification: 分类
AppendInfoId: 对应分类表的Id
##Orders
DeliveryState: 寄出/快递信息/寄到/ (付款)



