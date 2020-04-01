from __future__ import absolute_import
from celery.schedules import crontab

CELERY_BROKER_URL = 'redis://:1qaz@WSX@118.25.181.239:7778/3'

CELERY_RESULT_BACKEND = 'redis://:1qaz@WSX@118.25.181.239:7778/4'

CELERY_TASK_SERIALIZER = 'json'

CELERY_RESULT_SERIALIZER = 'json'

CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
timezone = "Asia/Shanghai"  # 时区设置
# 导入任务所在文件
imports = [
    "celerys.tasks",  # 导入py文件

]


# 需要执行任务的配置
beat_schedule = {
    "save": {
        "task": "celerys.tasks.test1",  #执行的函数
        "schedule": crontab(minute="*/1"),   # every minute 每分钟执行
        "args": ()  # # 任务函数参数
    },

}