from django.db import models
from organization.models import Teacher,City,CourseOrg
from tinymce.models import HTMLField
from datetime import datetime
# Create your models here.

class Course(models.Model):
    name =models.CharField(max_length=30,verbose_name="课程名")
    desc = models.CharField(max_length=50,verbose_name="课程描述")
    detail = HTMLField()
    is_banner = models.BooleanField(default=False,verbose_name="是否轮播")
    degree = models.CharField(
        max_length=5,
        choices=(
            ('pri','初级'),
            ('mid','中级'),
            ('hei','高级')
        )
    )
    students = models.IntegerField(default=0,verbose_name="学习人数")
    fav_nums = models.IntegerField(default=0,verbose_name="收藏人数")
    image = models.ImageField(null=True,blank=True,
        upload_to="course/couimage/%s"%(name),
        max_length=100,
        verbose_name="课程封面",
        default="default.png"
    )
    click_nums = models.IntegerField(default=0,verbose_name="浏览量")
    add_time = models.DateField(default=datetime.now,verbose_name="添加时间")
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,verbose_name="授课教师")
    course_org = models.ForeignKey(CourseOrg,on_delete=models.CASCADE,verbose_name="所属机构")
    tag = models.ManyToManyField(to='Tags')
    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class BannerCourse(Course):
    class Meta:
        verbose_name = "轮播课程"
        verbose_name_plural = verbose_name
        proxy =True #具备models功能，但不会生成新的表

# 章节
class Lesson(models.Model):
    # 因为一个课程对应很多章节。所以在章节表中将课程设置为外键。
    # 作为一个字段来让我们可以知道这个章节对应那个课程
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name="章节名")
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '《{0}》课程的章节{1}'.format(self.course, self.name)

# 每章视频
class Video(models.Model):
    # 因为一个章节对应很多视频。所以在视频表中将章节设置为外键。
    # 作为一个字段来存储让我们可以知道这个视频对应哪个章节.
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name=u"章节")
    name = models.CharField(max_length=100, verbose_name=u"视频名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    url = models.FileField(
        upload_to="course/video/%s"%(name,),
        verbose_name=u"视频文件",
        max_length=100)
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}章节的视频 >> {1}'.format(self.lesson, self.name)

#标签
class Tags(models.Model):
    name = models.CharField(max_length=20,verbose_name="标签名")
    class Meta:
        verbose_name = u"标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

