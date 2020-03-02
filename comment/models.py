from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class Comment(models.Model):
    content_type = models.ForeignKey(ContentType,on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type","object_id")

    content = models.TextField(verbose_name="评论内容")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="评论时间")
    comment_auth = models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name="评论者")

    class Meta:
        ordering = ["-create_time"]
        verbose_name = "评论列表"
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.comment_auth.username