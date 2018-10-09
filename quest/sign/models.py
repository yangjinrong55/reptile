from django.db import models

# Create your models here.
#发布会表
class Event(models.Model):
    # 发布会标题
    #objects = None
    name = models.CharField(max_length=100)
    #参加人数
    limit = models.IntegerField()
    #状态
    status = models.BooleanField()
    #地址
    address = models.CharField(max_length=200)
    #发布会时间
    time = models.DateTimeField('events time')
    #创建时间
    createTime = models.DateTimeField(auto_now=True)
    #peopleName = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#嘉宾表
class Guest(models.Model):
    #关联发布会Id
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    #姓名
    realname = models.CharField(max_length=100)
    #电话
    phone = models.CharField(max_length=60)
    #邮箱
    email = models.EmailField()
    #签到状态
    sign = models.BooleanField()
    #创建时间
    createTime = models.DateTimeField()
    class Meta:
        unique_together = ('event','phone')
    def __str__(self):
        return self.realname

