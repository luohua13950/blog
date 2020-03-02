from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.views import generic
from django.http import HttpResponse,JsonResponse
from .models import Tag,Post,Category,VisitorInfo
import markdown
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
import datetime
import json
from comment.models import Comment
from django.contrib.contenttypes.models import ContentType
from utils import common
from django.core import serializers
# Create your views here.
NUM = 10
def index(req,pk=1):
    post_list = Post.objects.all()
    pages = Paginator(post_list,6)
    try:
        page = pages.page(pk)
    except PageNotAnInteger:
        page = pages.page(1)
    except EmptyPage:
        page = pages.page(pages.num_pages)
    return render(req,"blog/index.html",context={"post_list":page})


@csrf_exempt
def detail(request,pk):
    keys = list(request.COOKIES.keys())
    ip = request.COOKIES.get("ip","") if  "ip" in keys else ""
    is_allow = request.COOKIES.get('is_allow',"") if  "is_allow" in keys else ""
    _unlock_time = request.COOKIES.get('unlock_time',"") if  "unlock_time" in keys else ""
    is_read = request.COOKIES.get(str(pk),"")

    #微秒格式化加了一个%f
    if _unlock_time:
        unlock_time = datetime.datetime.strptime(_unlock_time, "%Y-%m-%d %H:%M:%S.%f")
        if unlock_time and unlock_time < datetime.datetime.now():
            visited = VisitorInfo.objects.get(ip = ip)
            visited.is_allow = True
            visited.unlock_time = None
            visited.save()
        else:
            return render(request, "404.html")
    post = get_object_or_404(Post,pk=pk)
    ct = ContentType.objects.get_for_model(post)
    comment = Comment.objects.filter(content_type=ct, object_id=pk)

    next_post = post.get_next_post() or Post.objects.first()
    pre_post =  post.get_pre_post() or Post.objects.last()

    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    context = {"post": post, 'next_post': next_post, 'pre_post': pre_post}
    context.update({"comment":comment,"comment_count":comment.count()})
    resp = render(request, "blog/detail.html",context )
    if not is_read:
        post.views +=1
        post.save()
        resp.set_cookie(str(pk), ip, max_age=5 * 60)
    return resp

@csrf_exempt
def get_ip_info(request,pk):
    ip = request.POST.get("ip","")
    position = request.POST.get("position","")
    visited_time = datetime.datetime.now()
    threhold = datetime.timedelta(seconds=30)
    resp = JsonResponse({"result": "ok"})
    try:
        visited = VisitorInfo.objects.get(ip=ip)
        dd = datetime.datetime.now() - visited.visited_time
        if visited.unlock_time and not visited.is_allow and  visited.unlock_time < datetime.datetime.now():
            visited.is_allow = True
            visited.unlock_time = None
        if dd <threhold:
            visited.hit_frequency += 1
        else:
            if visited.hit_frequency >6:
                visited.is_allow = False
                timedelta = datetime.timedelta(days=1)
                visited.unlock_time = visited_time + timedelta
                visited.lock_numbers +=1
            visited.visited_time = visited_time
            visited.hit_frequency = 0

        resp.set_cookie("ip",visited.ip,max_age=100)
        resp.set_cookie("is_allow",visited.is_allow,max_age=100)
        if visited.unlock_time:
            resp.set_cookie("unlock_time",visited.unlock_time,max_age=100)
    except VisitorInfo.DoesNotExist:
        visited = VisitorInfo.objects.create(ip=ip, position=position, visited_time=visited_time, is_allow=True,
                                             lock_numbers=0, hit_frequency=0)
    #visited = VisitorInfo.objects.update_or_create(ip=ip,position=position,visited_time = visited_time,is_allow=True,lock_numbers=0,hit_frequency=0)
    visited.save()
    return resp


def error_views(request):
    context = {}
    context["error_message"] = "访问过于频繁！！"
    return render(request,"404.html",context=context)



def get_recent_post(request):
    data = serializers.serialize("json",Post.objects.all().order_by('-created_time')[:NUM])
    data = json.loads(data)
    data = get_urls(data)
    return JsonResponse(data,safe=False)


def get_hot_post(request):
    data = serializers.serialize("json",Post.objects.all().order_by('-views')[:NUM])
    data = json.loads(data)
    data = get_urls(data)
    return JsonResponse(data,safe=False)

def get_urls(query_set):
    for index,qt in enumerate(query_set):
        pk = qt["pk"]
        url = reverse("post:detail",kwargs={"pk":pk})
        query_set[index]["url"] = url
    return query_set


def display_category(request):
    return render(request,"blog/category.html")


@csrf_exempt
def get_category_data(request):
    page = request.POST.get("page","")
    keyword = request.POST.get("keyword","")
    data = {}
    num = 4
    if page:
        page = int(page)
        if keyword:
            cate = Category.objects.get(name=keyword)
            post_list = Post.objects.filter(category=cate).order_by("-istop")[page*num:(page+1)*num]
        else:
            post_list = Post.objects.all().order_by("-istop")[page*num:(page+1)*num]
        data = serializers.serialize("json",post_list)
        data = json.loads(data)
    return  JsonResponse(data,safe=False)


