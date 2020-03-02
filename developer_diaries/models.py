from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class DeveloperDiaries(models.Model):
    FUNCTION_TYPE=(
        ("OPT","优化"),
        ("NEW","新增"),
    )
    developer = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="开发者")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    planed_complete_time = models.DateTimeField(verbose_name="计划完成时间")
    is_completed = models.BooleanField(default=False,verbose_name="是否完成")
    optimize_or_new = models.CharField(max_length=30,choices=FUNCTION_TYPE,verbose_name="优化或新增")
    designation = models.CharField(max_length=100,verbose_name="功能名称")
    content = models.TextField(verbose_name="功能内容")
    istop = models.BooleanField(default=False,verbose_name="置顶")
    link = models.CharField(max_length=100,default="#",verbose_name="完成后记录过程的链接")

    class Meta:
        verbose_name = "开发者日志"
        verbose_name_plural = verbose_name
        ordering = ["-create_time"]

    def __str__(self):
        return self.designation+":"+self.get_optimize_or_new_display()