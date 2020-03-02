__author__ = 'luohua139'

from django.urls import path,re_path
from . import views
app_name = "comment"
urlpatterns =[
    path("comment/",views.comments,name = "comment"),
    path("delete_comment/",views.delete_comment,name = "delete_comment"),
]