from django.shortcuts import render,redirect
from .models import Comment
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.contenttypes.models import ContentType
from posts.models import Post
import datetime
from  utils import common
# Create your views here.

@csrf_exempt
def comments(request):
    data = {}
    context = request.POST.get("context","")
    object_id = request.POST.get("pk","")
    object_id = int(object_id) if object_id else ""
    content_type = request.POST.get("content_type","")
    data["context"] = context
    try:
        model = ContentType.objects.get(model=content_type).model_class()

        relate_model = model.objects.get(pk=object_id)
        ct = ContentType.objects.get_for_model(relate_model)
        comment_num = Comment.objects.filter(content_type=ct,object_id=object_id).count()
        user = request.user
        if user.is_authenticated:
            comment = Comment()
            comment.content = context
            comment.content_object = relate_model
            comment.comment_auth = user
            if common.comment_numbers(relate_model,object_id,user):
                comment.save()
                data["status"] = "success"
                data["time"] = common.process_time(comment.create_time)
                data["message"] = "评论成功！"
            else:
                data["status"] = "error"
                data["message"] = "你的评论过于频繁！"
            data["user"] = user.username
            data["comment_num"] = comment_num
        else:
            data["status"] = "error"
            data["message"] = "请先登录再评论！"
    except ContentType.DoesNotExist:
        data["status"] = "error"
        data["message"] = "评论失败！"
    return JsonResponse(data)

@csrf_exempt
def delete_comment(request):
    pk = request.POST.get("pk","")
    comment_id = request.POST.get("comment_id","")
    # model = ContentType.objects.get(model="post").model_class()
    data = {}
    try:
        if comment_id:
            comment = Comment.objects.get(pk=comment_id)
            comment.delete()
            data["status"] = "success"
            data["msg"] = "删除评论成功"
        else:
            data["status"] = "error"
            data["msg"] = "删除失败"
    except Comment.DoesNotExist:
        data["status"] = "error"
        data["msg"] = "删除失败,评论不存在,请刷新页面重试！"
    return JsonResponse(data)



