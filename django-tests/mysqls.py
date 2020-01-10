__author__ = 'luohua139'
import pymysql

def conn():
    con = pymysql.connect(host = "118.25.181.239",port=3306,user="luohua",password = "1qaz@WSX",db="wordpress")
    cur = con.cursor()
    sql ="select * from wp_users"
    ret = cur.execute(sql)
    print(cur.fetchall())


if __name__ == '__main__':
    conn()