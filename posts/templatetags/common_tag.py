from django import template
from posts.models import Post,Category,Tag
from config.models import Menu,DBConfig

register = template.Library()

@register.simple_tag
def get_recent_post(num=20):
    return Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def get_hot_post(num=20):
    return Post.objects.all().order_by('-views')[:num]

@register.simple_tag
def get_menu():
    return Menu.objects.all().order_by("id")