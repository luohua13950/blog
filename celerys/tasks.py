

# from django.conf import settings
# settings.configure()
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
django.setup()
from celerys.app import app
from proxies.models import Proxies
from django_redis import get_redis_connection
import datetime

@app.task
def test1():
    try:
        conn = get_redis_connection('default')
        total_prixes = conn.zrangebyscore("proxies",0,100,0,-1,withscores=True)
    except:
        return
    for prx in total_prixes:
        try:
            url = prx[0]
            score = int(prx[1])
            info_list = url.split(":")
            http_type = info_list[0]
            ip =info_list[1].replace("//","")
            port = info_list[2]
            valid_time = datetime.datetime.now()
            st = status(score)
            prx_info = {
                "host":ip,
                "http_type":http_type,
                "port":port,
                "score":score,
                "valid_time":valid_time,
                "status":st,
            }
            #defaults为要更新的值，http_type=http_type,host=ip为过滤
            flag = Proxies.objects.update_or_create(http_type=http_type,host=ip,defaults=prx_info)
            if flag:
                print(prx_info,"更新成功")
            else:
                print(prx_info, "无更新")
        except:
            continue
    print("保存成功")

def status(score):
    if score == 100:
        return "基本可用"
    elif 70 <score <=90:
        return "可能存活"
    elif 30<score<=70:
        return "基本不连通"
    elif 0<= score <30:
        return "即将移除此代理"
#celery -A celerys.app beat
#celery -A celerys.app worker --loglevel=info
if __name__ == '__main__':
    #test1()
    res = test1.delay()
    # print(res.result)
    #print(res.get())
    #print(app.conf)
    #ret = app.conf.humanize(with_defaults=False, censored=True)
    # ret = app.conf.table(with_defaults=False, censored=True)
    # print(ret)
    # now = datetime.datetime.now()
    # res = add.apply_async((3,6),countdown=10)
    # # res = add.apply_async((3,6),eta=datetime.timedelta(seconds=10))