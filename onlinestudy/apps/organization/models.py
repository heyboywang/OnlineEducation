from django.db import models
from datetime import datetime
from tinymce.models import HTMLField
# Create your models here.

#城市
class City(models.Model):
    name = models.CharField(max_length=20,verbose_name="城市名")
    desc = models.CharField(max_length=50,verbose_name="城市描述",null=True,blank=True)
    add_time = models.DateField(default=datetime.now,verbose_name="添加时间")
    class Meta():
        verbose_name = "城市"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

#课程机构
class CourseOrg(models.Model):
    name = models.CharField(max_length=50,verbose_name="机构名")
    desc = HTMLField()
    category = models.CharField(
        max_length=20,
        choices=(
            ('pxjg','培训机构'),
            ('gx','高校'),
            ('gr','个人')
        ),
        default='pxjg',
        verbose_name="机构类别",
    )
    click_nums = models.IntegerField(default=0,verbose_name="点击数")
    fav_nums = models.IntegerField(default=0,verbose_name="收藏数")
    image = models.ImageField(
        upload_to="courseimages/%s/"%(name,),
        verbose_name="封面图",
        max_length=100,
    )
    address = models.CharField(max_length=50,null=True,blank=True)
    #拥有外键所在城市
    city = models.ForeignKey(City,on_delete=models.CASCADE,verbose_name="所在城市")
    #学生人数
    user_nums = models.IntegerField(default=0,verbose_name="学习人数")
    course_nums = models.IntegerField(default=0,verbose_name="课程数量")
    add_time = models.DateField(default=datetime.now,verbose_name="创建时间")

    class Meta():
        verbose_name = "课程机构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

#讲师
class Teacher(models.Model):
    name = models.CharField(max_length=20,verbose_name="讲师名字")
    work_year = models.IntegerField(default=0,verbose_name="工作时长")
    work_company = models.CharField(max_length=50,verbose_name="工作公司")
    work_position = models.CharField(max_length=20,verbose_name="工作职位")
    age = models.IntegerField(default=0,verbose_name="年龄")
    points = models.CharField(max_length=50,verbose_name="教学特点")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    image = models.ImageField(
        upload_to="teaimage/%s"%(name,),
        default="",
        verbose_name="头像",
        max_length=100,
    )
    add_time = models.DateField(default=datetime.now,verbose_name="入职时间")

    class Meta():
        verbose_name = "讲师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



