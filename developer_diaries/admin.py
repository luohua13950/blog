from django.contrib import admin
from developer_diaries.models import DeveloperDiaries
# Register your models here.
class DeveloperDiariesAdmin(admin.ModelAdmin):
    list_display = ["developer","create_time","designation","content"]


admin.site.register(DeveloperDiaries)