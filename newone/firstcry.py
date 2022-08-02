import requests
from lxml import html
import pandas
import os
import math, json, time

url = "https://www.firstcry.com/tops-and-t-shirts/6/26?scat=26&gender=boy,unisex&sort=bestseller&ref2=menu_dd_boy-fashion_t-shirt_H#scat=26@@@@@@@@@@1@0@20@@@@@@@@@@&rating=&sort=bestseller&&vi=three&pmonths=&cgen=&cat=6&skills=&measurement=&material=&Color=&Age=&gender=both,male&ser=&premium=&deliverytype=&PageNo=1&scrollPos=228&pview=&tc=14599"
r = requests.get(url)
# print(r.text)
root = html.fromstring(r.content)
print(root.xpath("//div[@class='list_block lft fasnlist']"))

_len = len(root.xpath("//div[@class='list_block lft fasnlist']"))
print(_len)
final_list = []
for x in range(_len):
    _dict = {}
    title = root.xpath("//div[@class='list_block lft fasnlist']//div[@class='li_txt1 wifi lft']/a/@title")[x]
    _dict["title"] = title
    # _price = {}
    price =  root.xpath("//div[@class='list_block lft fasnlist']//div[@class='rupee fw lft']/span/a/text()")[x]
    _dict["price"] = price
    final_list.append(_dict)
    # final_list.append(_price)
    # print(final_list)
print(final_list)

#df = pandas.DataFrame(final_list)
#df.to_csv(r"C:\Users\admin\PycharmProjects\pythonProject\firstcry.csv",  index=False)
#print("@@@@@@@", final_list)
#print(df.head(7))