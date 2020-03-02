from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Menu(models.Model):
    menu_name = models.CharField(max_length=100,verbose_name="菜单名称")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="添加时间")
    create_user = models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name="添加人")
    url = models.CharField(max_length=100,blank=True,verbose_name="url")
    sub_menu = models.BooleanField(default=False,verbose_name="是否有下级菜单")

    class Meta:
        verbose_name = "导航菜单表"
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.menu_name


class DBConfig(models.Model):
    db_type = models.CharField(max_length=48,default="mysql",verbose_name="数据库类型")
    host = models.CharField(max_length=100,verbose_name="ip地址")
    port = models.PositiveIntegerField(default=3306,verbose_name="端口号")
    username = models.CharField(max_length=100,verbose_name="用户名")
    password = models.CharField(max_length=100,verbose_name="密码")

    class Meta:
        verbose_name = "数据库信息配置表"
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.db_type +":"+self.host



class ErrorCode(models.Model):
    code = models.PositiveIntegerField(verbose_name="错误码")
    context = models.CharField(max_length=50,verbose_name="错误内容")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="添加时间")

    class Meta:
        verbose_name = "错误码表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.code)+":"+self.context