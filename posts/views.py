from django.shortcuts import render
from django.views import generic
# Create your views here.
def index(req):
    return render(req,"blog/detail.html")



def detail(request,pk):
    pass