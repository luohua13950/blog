# Generated by Django 2.2.6 on 2020-03-23 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proxies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proxies',
            name='status',
            field=models.CharField(default='基本可用', max_length=100, verbose_name='代理状态'),
        ),
    ]
