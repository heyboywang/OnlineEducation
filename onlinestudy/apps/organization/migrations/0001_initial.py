# Generated by Django 2.2.1 on 2019-05-08 01:30

import datetime
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='城市名')),
                ('desc', models.CharField(blank=True, max_length=50, null=True, verbose_name='城市描述')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '城市',
                'verbose_name_plural': '城市',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='讲师名字')),
                ('work_year', models.IntegerField(default=0, verbose_name='工作时长')),
                ('work_company', models.CharField(max_length=50, verbose_name='工作公司')),
                ('work_position', models.CharField(max_length=20, verbose_name='工作职位')),
                ('age', models.IntegerField(default=0, verbose_name='年龄')),
                ('points', models.CharField(max_length=50, verbose_name='教学特点')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击数')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏数')),
                ('image', models.ImageField(default='', upload_to='teaimage/<django.db.models.fields.CharField>', verbose_name='头像')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='入职时间')),
            ],
            options={
                'verbose_name': '讲师',
                'verbose_name_plural': '讲师',
            },
        ),
        migrations.CreateModel(
            name='CourseOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='机构名')),
                ('desc', tinymce.models.HTMLField()),
                ('category', models.CharField(choices=[('pxjg', '培训机构'), ('gx', '高校'), ('gr', '个人')], default='pxjg', max_length=20, verbose_name='机构类别')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击数')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏数')),
                ('image', models.ImageField(upload_to='courseimages/<django.db.models.fields.CharField>/', verbose_name='封面图')),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('user_nums', models.IntegerField(default=0, verbose_name='学习人数')),
                ('course_nums', models.IntegerField(default=0, verbose_name='课程数量')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.City', verbose_name='所在城市')),
            ],
        ),
    ]
