import time

import requests
from lxml import html
import pandas
#user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
#ROBOTSTXT_OBEY = True
#import scrapy
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding" : "gzip, deflate, br",
    "accept-language" : "en-US,en;q=0.9",
    "cache-control" : "max-age=0",
    "cookie" : "fre=0; rd=1380000; zl=en; fbtrack=830174538e1706ff0268a409f6d683e8; _ga=GA1.2.1421769944.1644070341; _gcl_au=1.1.882544753.1644070341; _fbp=fb.1.1644070342720.889695564; uspl=true; G_ENABLED_IDPS=google; zhli=1; _gcl_aw=GCL.1644120211.Cj0KCQiA3fiPBhCCARIsAFQ8QzVrXM6nmtexjN8lKheMh4sG2cN0Wk9NPiJOFB01KPOhOuAdseuK6hIaAv-BEALw_wcB; _gac_UA-19617341-21=1.1644120211.Cj0KCQiA3fiPBhCCARIsAFQ8QzVrXM6nmtexjN8lKheMh4sG2cN0Wk9NPiJOFB01KPOhOuAdseuK6hIaAv-BEALw_wcB; _gac_UA-19617341-30=1.1644120211.Cj0KCQiA3fiPBhCCARIsAFQ8QzVrXM6nmtexjN8lKheMh4sG2cN0Wk9NPiJOFB01KPOhOuAdseuK6hIaAv-BEALw_wcB; _gid=GA1.2.816963502.1644306234; PHPSESSID=0932bdf234bc8cdcafd3d3becb90a8e2; csrf=b316b7b50baa8bd0729c9269b2b7a9e6; fbcity=11302; ltv=11302; lty=11302; locus=%7B%22addressId%22%3A0%2C%22lat%22%3A25.169053%2C%22lng%22%3A75.849932%2C%22cityId%22%3A11302%2C%22ltv%22%3A11302%2C%22lty%22%3A%22city%22%2C%22fetchFromGoogle%22%3Afalse%2C%22dszId%22%3A19156%2C%22fen%22%3A%22Kota%22%7D; AWSALBTG=4yS9ZePK51EfO5VzidaPSA9831/+SLOxdZ01Cc/s7aFGAD+GXGJtd+ikE7r2tNYGCk4Acf3bcicR401XPU0Z83L2RCYmm4FrH84aJSaO0DvDLKbF78HlMmW3X7YXu3kBFkeM5APGLJ/kFPRUdTWG6zgMqqtEEyHUedbNuJmnvjGS; AWSALBTGCORS=4yS9ZePK51EfO5VzidaPSA9831/+SLOxdZ01Cc/s7aFGAD+GXGJtd+ikE7r2tNYGCk4Acf3bcicR401XPU0Z83L2RCYmm4FrH84aJSaO0DvDLKbF78HlMmW3X7YXu3kBFkeM5APGLJ/kFPRUdTWG6zgMqqtEEyHUedbNuJmnvjGS",
    "sec-ch-ua" : '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    "sec-ch-ua-mobile" : "?0",
    "sec-ch-ua-platform" : "Windows",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user" : "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36}"
}
url= "https://www.zomato.com/delivery-cities"
r=requests.get(url, headers=headers).content
time.sleep(2)
# print(r)
# o = open("a.txt", "w")
# o.write(str(r))
root = html.fromstring(r)
print(root.xpath("//h1[text()='Cities We Deliver To']/following-sibling::div/a[text()='Salem']/@href"))