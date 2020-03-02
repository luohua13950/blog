__author__ = 'luohua139'

from django.urls import path,re_path
from . import views
app_name = "post"
urlpatterns =[
    path("",views.index,name = "index"),
    path("post/<int:pk>/",views.detail,name = "detail"),
    path("index/<int:pk>",views.index,name = "pages"),
    path("ips/<int:pk>/",views.get_ip_info,name = "ip"),
    path("error/",views.error_views,name = "error"),
    path("recent/",views.get_recent_post,name = "recent"),
    path("hot/",views.get_hot_post,name = "hot"),
    path("category/",views.display_category,name = "category"),
    path("spider/",views.display_category,name = "spider"),
    path("blog/",views.display_category,name = "spider"),
    path("get_category_data/",views.get_category_data,name = "get_category"),
    #re_path("post/(?P<pk>[0-9]+)/",views.detail,name = "detail"),
]