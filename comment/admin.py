from django.contrib import admin
from .models import Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ["content","create_time","comment_auth"]


admin.site.register(Comment)
