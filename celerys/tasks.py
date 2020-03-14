from celery import Celery
import datetime
app = Celery("tasks")
app.config_from_object('celeryconfig', namespace='CELERY')


@app.task()
def add(x,y):
    return x+y

@app.task()
def _add(x,y):
    return x+y

if __name__ == '__main__':
    # res = add.delay(3,4)
    # print(res.result)
    #print(res.get())
    print(app.conf)
    # ret = app.conf.humanize(with_defaults=False, censored=True)
    # table = app.conf.table(with_defaults=False, censored=True)
    # print(table)
    # now = datetime.datetime.now()
    # res = add.apply_async((3,6),countdown=10)
    # # res = add.apply_async((3,6),eta=datetime.timedelta(seconds=10))