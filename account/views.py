from django.shortcuts import render,reverse,redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def logins(request):
    username = request.POST.get("username","")
    password = request.POST.get("password","")
    referer = request.META.get("HTTP_REFERER","/")
    user = authenticate(username=username, password=password)
    data = {}

    if user:
        login(request,user)
        data["status"] = "success"
        data["msg"] = "登录成功"
    else:
        data["status"] = "error"
        data["msg"] = "用户名或密码错误"

    data["referer"] = referer if "login" not in referer else "/"
    return JsonResponse(data)


def logouts(request):
    logout(request)
    referer = request.META.get("HTTP_REFERER", "")
    if referer:
        return redirect(referer)
    return redirect(reverse("post:index"))

@csrf_exempt
def register(request):
    data = {}
    username = request.POST.get("username","")
    password = request.POST.get("password","")
    password2 = request.POST.get("password2","")
    email = request.POST.get("email","")
    referer = request.META.get("HTTP_REFERER","/")
    if all([username,password,password2,email]):
        if password == password2:
            if User.objects.filter(username=username).count() > 0:
                data["status"] = "error"
                data["msg"] = "注册失败，用户已存在！"
            elif User.objects.filter(email=email).count() >0:
                data["status"] = "error"
                data["msg"] = "该邮箱已注册！"
            else:
                user = User.objects.create_user(username=username,password=password,email=email,is_active=True,is_superuser=False,is_staff=False)
                data["status"] = "success"
                data["msg"] = "注册成功,5秒后自动跳转到首页"
                login(request, user)
        else:
            data["status"] = "error"
            data["msg"] = "注册失败，密码不一致！"
    else:
        data["status"] = "error"
        data["msg"] = "注册失败，请输入完整信息"
    data["referer"] = referer
    return JsonResponse(data)

def to_login(request):
    login_url =reverse("account:login")
    register_url =reverse("account:register")
    referer = request.META.get("HTTP_REFERER", "") if request.META.get("HTTP_REFERER", "") else "/"
    return render(request,"blog/login.html",{"url":login_url,"r_url":register_url,"ref":referer})