'''
任务 task
本质是一个python函数 将耗时操作封装成一个函数

队列	 queue
将要执行的任务放到队列里面去

工人 worker
负责执行队列中的任务

代理 broker
负责调度，在部署环境中使用redis
'''
#在工程目录下的project目录下创建celery.py文件中添加
from __future__ import absolute_import

import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'whthas_home.settings')
app = Celery('portal')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda:settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
	print('Request:{0!r}'.format(self.request))
#在工程目录下的project目录下__ init.py __文件中添加S
from .celery import app as celery_app