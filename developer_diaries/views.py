from django.shortcuts import render,reverse
from .models import DeveloperDiaries
from django.contrib.auth.models import User
# Create your views here.
import markdown
def dev_diaries(request):
    dev_list = DeveloperDiaries.objects.all().order_by("-istop","create_time")
    for dev in dev_list:
        dev.content = markdown.markdown(dev.content,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])

    return render(request,"blog/devlog.html",{"dev_list":dev_list})