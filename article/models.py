# coding=utf-8
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)                #博客标题
    category = models.CharField(max_length=50,blank=True)   #博客标签
    date_time = models.DateTimeField(auto_now_add=True)     #博客日期
    content = models.TextField(blank=True,null=True)        #博客正文

    def __unicode__(self):
        return self.title

class Meta:
    ordering=['-date_time']