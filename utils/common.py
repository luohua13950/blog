import datetime
from comment.models import Comment
from django.contrib.contenttypes.models import ContentType
def process_time(dest_time):
    now = datetime.datetime.now().date()
    dst = dest_time.date()
    sub = now.__sub__(dst).days
    if sub == 0:
        return "今天"
    elif sub >365:
        month = int(sub / 365)
        return str(month) + "年前"
    elif sub >30:
        month = int(sub/30)
        return str(month)+"个多月前"



def comment_numbers(objects,pk,user):
    # model = ContentType.objects.get(model=content_type).model_class()
    # objects = model.objects.get(pk=pk)
    ct = ContentType.objects.get_for_model(objects)
    comment = Comment.objects.filter(content_type=ct,object_id=pk,comment_auth=user).order_by("-create_time")
    if comment.count()>0:
        timedelta = datetime.timedelta(minutes=5)
        now = datetime.datetime.now()
        if now - comment.first().create_time >timedelta:
            return True
        else:
            return False
    return True



def get_username(data):
    for dt in data:
        pass