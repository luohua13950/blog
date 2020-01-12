__author__ = 'luohua139'

from django.urls import path
from . import views
app_name = "post"
urlpatterns =[
    path("",views.index,name = "index"),
    path("post/<int:pk>/",views.detail,name = "detail"),
]