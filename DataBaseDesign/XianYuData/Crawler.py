# -*- coding: utf-8 -*-
import random
from urllib import request,parse
import base64
import urllib.request
import os
import yaml
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup

class Crawler():
	executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver"
	indexHtml = 'https://2.taobao.com/'
	yamlpath = ""
	def __init__(self):
		return 
	def details(self, browser, info, path):
		browser.get(path)
		time.sleep(3+random.random())
		browser.execute_script('window.scrollBy(0, 800)')
		time.sleep(2+random.random())
		
		bsObj = BeautifulSoup(browser.page_source)		
		
		seller_info = bsObj.find("div",{"class":"seller-info"})
		print(seller_info)
		b = b'/:?=&#'
		img_url = parse.quote("https:"+seller_info.find("img")["src"], b)
		info["seller-icon"] = "<img src=\"data:image/jpg;base64,"+base64.b64encode(urllib.request.urlopen(img_url).read()).decode("utf-8")+"\"/>\n"
		info["seller-details"] = seller_info.find("div",{"class":"details"}).get_text()
		
		info["idle-info"] = bsObj.find("ul",{"class":"idle-info"}).get_text()
		info["describe"] = bsObj.find("div",{"class":"describe"}).get_text()
		
		return info
		
	def IndexPage(self):
		browser = webdriver.Chrome(self.executable_path)
		
		browser.get(self.indexHtml)		
		time.sleep(10)
		
		for i in range(1, 8):
			browser.execute_script('window.scrollBy(0, 800)')
			time.sleep(1)
			
		brief_info = open("brief_info2.html","a+",encoding='utf-8')
		bsObj = BeautifulSoup(browser.page_source)
		for itemlists in bsObj.findAll("ul",{"class":"J_ItemList item-list"}):
			items=itemlists.findAll("li",{"class":"item"})
			for item in items:
				title = item.find("p",{"class":"title"}).get_text()
				price = item.find("p",{"class":"price"}).get_text()
				img = urllib.request.urlopen("http:"+item.find("img")["src"]).read()
				base64_img = base64.b64encode(img)
				info = {"title":title,
						"price":price,
						"img": "<img src=\"data:image/jpg;base64,"+base64_img.decode("utf-8")+"\"/>"}
				#info = self.details(browser, info, "https:"+item.find("a")["href"])
				
				brief_info.write(str(info)+"<br>\n")
		brief_info.close()
	

	
if __name__=='__main__':
	c = Crawler()
	for i in range(10):
		c.IndexPage()
	
