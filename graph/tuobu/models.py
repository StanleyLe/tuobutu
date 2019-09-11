from django.db import models

# Create your models here.


class Graph(models.Model):
    graph_json = models.TextField(verbose_name='拓补图的json数据')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    objects = models.Manager()