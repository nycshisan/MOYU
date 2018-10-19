#数据库设计说明
##Users table
UserType : 管理员(0)或普通用户(1)
PhoneNumber : 预计用手机号登陆(或邮箱)
BuyerId/SellerId : 已删除
IsIdentified: 是(1)否(0)实名
##Items table
IsForRent: 是(1)否(0)租用
ShortCut: 一张图片或缩略图
Place: 发布地点
BaoYou: 是(1)否(0)包邮
Negotiation: 可(1)否(0)议价
Classification: 分类
AppendInfoId: 对应分类表的Id,暂无
##Orders
DeliveryState: 寄出/快递信息/寄到/ (付款)
Bey_UserId/Sel_UserId: 对应买卖方UserId
## 多余的属性
为了考虑周全, 才添加了许多可能用到,但是可以为空的属性, 如IsForRent, IsVip 等. 但在实际插入操作用, 可以不考虑这些属性.
# 闲鱼数据抓取
因为是非法爬虫, 所以数据不多
##./XianYuData/brief_info.html
从详细页面抓取, 数据较少,格式(例)为:
{'title': '尼康D850搭配24-70', 
'price': '¥14162', 
'img': '此处为html标签img的base64编码格式,可以直接在网页上显示',
'seller-icon': '空或同上', 
'seller-details': '空或可能包含性别昵称', 
'idle-info': '\n\n成\u3000\u3000色：\n非全新\n\n\n所\xa0\xa0在\xa0\xa0地：\n浙江金华 浦江县\n\n\n联系方式：\n\n旺旺离线\n\n\n\n交易方式：\n在线交易\n\n\n \t\t\t\t\t至 上海\n\n快递:免运费\n\n', 
'describe': ' 有正规全国联保发票，箱说齐全.还有一些多余配件.聊的来的可以全部赠送. 工作原因不怎么长在线请谅解有需要的朋友可以＋我V 171 **** 0565 '}
##./XianYuData/brief_info2.html
从首页抓取, 数据较多(其实也不多), 格式为:
{'title': '尼康D850搭配24-70', 
'price': '¥14162', 
'img': 'Base64编码'
}
## 
编码为utf-8, 数据在python中存储为字典直接输出,
可以用yaml等工具读入