from django.contrib import admin
from .models import Menu,DBConfig,ErrorCode
# Register your models here.
class ConfigAdmin(admin.ModelAdmin):
    list_display = ["menu_name","create_time","create_user","url"]

admin.site.register(Menu)
admin.site.register(DBConfig)
admin.site.register(ErrorCode)