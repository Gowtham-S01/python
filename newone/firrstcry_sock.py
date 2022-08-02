import requests
from lxml import html
import pandas
import os
import math, json, time

url="https://www.firstcry.com/socks-and-tights/6/238?scat=238&gender=boy,unisex&sort=bestseller&ref2=menu_dd_boy-fashion_socks_V"
r = requests.get(url)
# print(r.text)
root = html.fromstring(r.content)
print(root.xpath("//div[@class='option-container allsubmenu1-1']//li/a[@title='Socks']/@href"))
_len=len(root.xpath("//div[@class='list_block lft fasnlist']//div[@class='list_img wifi']/a/img"))
_list=[]
print(len(root.xpath("//div[@class='list_block lft fasnlist']")))


for x in root.xpath("//div[@class='list_block lft fasnlist']"):
    _dict={}
    image= x.xpath(".//div[@class='list_img wifi']/a/img/@src")

    _dict["Image"]=image[0]
    title= x.xpath(".//div[@class='list_img wifi']/a/img/@title")
    _dict["title"]=title[0]
    price= x.xpath(".//div[@class='rupee fw lft']/span[@class='r1 B14_42']/a/text()")
    _dict["price"]=price
    club_price = x.xpath(".//div[@class='club-block']//span[@class='r1 B12_blue']/a/text()")
    _dict["Club Price"]=club_price

    _list.append(_dict)

print(_list)

df = pandas.DataFrame(_list)
df.to_csv(r"C:\Users\gowth\PycharmProjects\newone\firstcrysocks.csv",  index=False)
#print("@@@@@@@",_list)
print(df.head(80))