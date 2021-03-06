# Generated by Django 2.2.6 on 2020-03-01 20:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.CreateModel(
            name='VisitorInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(verbose_name='访问ip')),
                ('position', models.CharField(blank=True, max_length=100, verbose_name='访问者位置')),
                ('visited_time', models.DateTimeField(blank=True, null=True, verbose_name='访问时间')),
                ('first_visited', models.DateTimeField(auto_now_add=True, verbose_name='第一次访问时间')),
                ('visited_numbers', models.PositiveIntegerField(blank=True, null=True, verbose_name='访问次数')),
                ('is_allow', models.BooleanField(blank=True, null=True, verbose_name='是否允许访问')),
                ('unlock_time', models.DateTimeField(blank=True, null=True, verbose_name='解除封禁时间')),
                ('lock_numbers', models.PositiveIntegerField(blank=True, null=True, verbose_name='被封禁次数')),
                ('hit_frequency', models.PositiveIntegerField(blank=True, null=True, verbose_name='访问频率')),
            ],
            options={
                'verbose_name': '游客访问信息',
                'verbose_name_plural': '游客访问信息',
                'ordering': ['first_visited'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='标题')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('body', models.TextField(verbose_name='正文')),
                ('excerpt', models.CharField(blank=True, max_length=200, verbose_name='摘要')),
                ('views', models.IntegerField(verbose_name='浏览次数')),
                ('cover_of_post', models.CharField(default='../../static/blog/img/py1.jpg', max_length=100, verbose_name='文章封面')),
                ('istop', models.BooleanField(default=False, verbose_name='是否置顶')),
                ('origin_or_reprint', models.CharField(choices=[('ORG', '原创'), ('RPT', '转载')], default='ORG', max_length=20, verbose_name='原创或转载')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Category', verbose_name='分类')),
                ('tags', models.ManyToManyField(blank=True, to='posts.Tag', verbose_name='标签')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'ordering': ['id'],
            },
        ),
    ]
