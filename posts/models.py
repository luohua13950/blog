from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(verbose_name="标题",max_length=200)
    created_time = models.DateTimeField(verbose_name="创建时间",auto_now_add=True)
    modify_time = models.DateTimeField(verbose_name="修改时间",auto_now=True)
    body = models.TextField(verbose_name="正文")
    excerpt = models.CharField(verbose_name="摘要",max_length=200,blank=True)
    author = models.ForeignKey(User,verbose_name="作者",on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag,verbose_name="标签",blank=True)
    category = models.ForeignKey(Category,verbose_name="分类",on_delete=models.CASCADE)
    views = models.IntegerField(verbose_name="浏览次数")


    def __str__(self):
        return self.title

    def get_absulute_url(self):
        return reverse("post:detail",kwargs={"pk":self.pk})
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name