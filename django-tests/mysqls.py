__author__ = 'luohua139'
import pymysql
import requests
def conn():
    con = pymysql.connect(host = "118.25.181.239",port=3306,user="luohua",password = "1qaz@WSX",db="wordpress")
    cur = con.cursor()
    sql ="select * from wp_users"
    ret = cur.execute(sql)
    print(cur.fetchall())

def req():
    url = "http://127.0.0.1:8000/post/5/"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    resp = requests.get(url,headers=headers)
    print(resp.status_code)

if __name__ == '__main__':
    for i in range(10):
        req()