from django.db import models

# Create your models here.
class Proxies(models.Model):
    http_type = models.CharField(max_length=30,verbose_name="代理类型")
    host = models.CharField(max_length=100,verbose_name="ip地址")
    port = models.CharField(max_length=30,verbose_name="端口")
    score = models.PositiveIntegerField(verbose_name="得分")
    valid_time = models.DateTimeField(verbose_name="验证时间")
    status = models.CharField(max_length=100,default="基本可用",verbose_name="代理状态")

    class Meta:
        verbose_name = "免费代理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}:{}:{}--->{}".format(self.http_type,self.host,self.port,str(self.score))