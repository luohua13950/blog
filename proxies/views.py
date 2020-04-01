from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.core.cache import cache
from django_redis import get_redis_connection
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Proxies
# Create your views here.
def get_proxies(request,pg):
    if not pg:
        pg =1
    if request.user.is_authenticated:
        proxies = Proxies.objects.all().order_by("-score")
        pages = Paginator(proxies, 100)
        try:
            page = pages.page(pg)
        except PageNotAnInteger:
            page = pages.page(1)
        except EmptyPage:
            page = pages.page(pages.num_pages)
    else:
        proxies = Proxies.objects.all().order_by("score")[:100]
        pages = Paginator(proxies, 100)
        page = pages.page(1)
    prx = {"proxies":page}
    return render(request,"blog/proxies/proxies.html",prx)