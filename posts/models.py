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
    POST_TYPE=(
        ("ORG","原创"),
        ("RPT","转载"),
    )
    title = models.CharField(verbose_name="标题",max_length=200)
    created_time = models.DateTimeField(verbose_name="创建时间",auto_now_add=True)
    modify_time = models.DateTimeField(verbose_name="修改时间",auto_now=True)
    body = models.TextField(verbose_name="正文")
    excerpt = models.CharField(verbose_name="摘要",max_length=200,blank=True)
    author = models.ForeignKey(User,verbose_name="作者",on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag,verbose_name="标签",blank=True)
    category = models.ForeignKey(Category,verbose_name="分类",on_delete=models.CASCADE)
    views = models.IntegerField(verbose_name="浏览次数")
    cover_of_post = models.CharField(max_length=100,default="../../static/blog/img/py1.jpg",verbose_name="文章封面")
    istop = models.BooleanField(default=False,verbose_name="是否置顶")
    origin_or_reprint = models.CharField(max_length=20,default="ORG",choices=POST_TYPE,verbose_name="原创或转载")

    def __str__(self):
        return self.title

    def get_absulute_url(self):
        return reverse("post:detail",kwargs={"pk":self.pk})

    def get_next_post(self):
        return Post.objects.filter(id__gt=self.pk).order_by("id").first()

    def get_pre_post(self):
        return Post.objects.filter(id__lt=self.pk).order_by("id").last()

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ["id"]


class VisitorInfo(models.Model):
    ip = models.GenericIPAddressField(verbose_name="访问ip")
    position = models.CharField(max_length=100,blank=True,verbose_name="访问者位置")
    visited_time = models.DateTimeField(null=True,blank=True,auto_now=False,auto_now_add=False,verbose_name="访问时间")
    first_visited = models.DateTimeField(blank=True,auto_now_add=True,verbose_name="第一次访问时间")
    visited_numbers = models.PositiveIntegerField(null=True,blank=True,verbose_name="访问次数")
    is_allow = models.BooleanField(null=True,blank=True,verbose_name="是否允许访问")
    unlock_time = models.DateTimeField(null=True,blank=True,verbose_name="解除封禁时间")
    lock_numbers = models.PositiveIntegerField(null=True,blank=True,verbose_name="被封禁次数")
    hit_frequency = models.PositiveIntegerField(null=True,blank=True,verbose_name="访问频率")

    class Meta:
        ordering = ["first_visited"]
        verbose_name = "游客访问信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ip+":"+self.position