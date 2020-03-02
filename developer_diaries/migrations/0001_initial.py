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
            name='DeveloperDiaries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('planed_complete_time', models.DateTimeField(verbose_name='计划完成时间')),
                ('is_completed', models.BooleanField(default=False, verbose_name='是否完成')),
                ('optimize_or_new', models.CharField(choices=[('OPT', '优化'), ('NEW', '新增')], max_length=30, verbose_name='优化或新增')),
                ('designation', models.CharField(max_length=100, verbose_name='功能名称')),
                ('content', models.TextField(verbose_name='功能内容')),
                ('istop', models.BooleanField(default=False, verbose_name='置顶')),
                ('link', models.CharField(default='#', max_length=100, verbose_name='完成后记录过程的链接')),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='开发者')),
            ],
            options={
                'verbose_name': '开发者日志',
                'verbose_name_plural': '开发者日志',
                'ordering': ['-create_time'],
            },
        ),
    ]
