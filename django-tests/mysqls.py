__author__ = 'luohua139'
import pymysql
import requests
import json
from bs4 import BeautifulSoup,Tag
from django.views.decorators.cache import cache_page
def req():
    url = "http://www.happyhong.cn/post/14/"
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
              }

    resp = requests.get(url,headers=headers)
    bs_html = BeautifulSoup(resp.text,"html.parser")
    print(bs_html.a)
    print(type(bs_html.a))
    #print([bs for bs in dir(bs_html) if not bs.startswith("_")])


if __name__ == '__main__':
    req()