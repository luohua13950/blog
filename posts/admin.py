from django.contrib import admin

# Register your models here.
from .models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modify_time', 'category', 'author']
    fields = ['title', 'body', 'excerpt', 'category', 'tags']

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)