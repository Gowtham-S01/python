
import requests
from lxml import html
import pandas
import os
import math, json, time

url="https://www.firstcry.com/?ref2=menu_dd_catlanding"
r = requests.get(url)
# print(r.text)
root = html.fromstring(r.content)
print(root.xpath("//div[@class='menu-container']"))
_len=len(root.xpath("//div[@class='menu-container']//li[@class='M14_42 categry']/a/text()"))
_list=[]
for x in range(_len-1):
    _dict={}
    name= root.xpath("//div[@class='menu-container']//li[@class='M14_42 categry']/a/text()")[x]
    _dict["Category Name"]=name


    link=root.xpath("//div[@class='menu-container']//li[@class='M14_42 categry']/a/@href")[x]
    _dict["Category Link"] =link
    _list.append(_dict)
print(_list)

df = pandas.DataFrame(_list)
df.to_csv(r"C:\Users\gowth\PycharmProjects\newone\categories.csv",  index=True)
print("@@@@@@@",_list)
print(df.head())