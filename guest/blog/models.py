from django.db import models

# Create your models here.
class Blog(models.Model):
    #ID = models.CharField(max_length=100) # 序列号
    flag_choise=(('T', 'test'), ('L', 'live'), ('W', 'work'), ('P', 'personal'), ('H', 'habit'))
    #blog_id = models.AutoField(primary_key=True) 如果不指定主键,Django 会自动添加一个IntegerField 字段做为主键
    blog_title = models.CharField(max_length=150) # 标题
    blog_content= models.TextField() # 内容
    create_time = models.DateTimeField(auto_now=True) # 创建时间（自动获取当前时间）
    flag = models.CharField(max_length=10, choices=flag_choise) # 标记

    def __str__(self):
        return self.blog_title






