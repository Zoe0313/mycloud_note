from django.db import models

# Create your models here.
from user.models import User

class Note(models.Model):
    title = models.CharField('标题',max_length=100,default='')
    content = models.TextField('内容',default='')
    create_time = models.DateTimeField('创建时间',auto_now_add=True)
    mod_time = models.DateTimeField('修改时间',auto_now=True)
    author = models.ForeignKey(User) #一对多
    def __str__(self):
        return self.title