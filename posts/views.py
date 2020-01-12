from django.shortcuts import render,get_object_or_404
from django.views import generic
from .models import Tag,Post,Category
import markdown
# Create your views here.
def index(req):
    post_list = Post.objects.all()

    return render(req,"blog/index.html",context={"post_list":post_list})



def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request,"blog/detail.html",{"post":post})