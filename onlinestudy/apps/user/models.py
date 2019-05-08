from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#用户表
class Suser(User):
    nick_name = models.CharField(max_length=20,verbose_name="昵称",default="")
    birthday = models.DateField(verbose_name="生日",null=True,blank=True)
    gender = models.CharField(
        max_length=5,
        choices=(
            ("man","男"),
            ("woman","女")
        ),
        verbose_name="性别",
        default="man"
    )
    address = models.CharField(max_length=100,blank=True,null=True,default="")
    phone = models.CharField(max_length=11,blank=True,null=True,default="")
    headimage = models.ImageField(
        upload_to="headimage/%s/"%(nick_name,),
        max_length=100,
        default="default.png"
    )

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nick_name