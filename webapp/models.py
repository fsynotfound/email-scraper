from django.db import models

# 创建一个数据库模型
class EmailEntry(models.Model):    
    email = models.EmailField()
    source_url = models.URLField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.email# Create your models here.
