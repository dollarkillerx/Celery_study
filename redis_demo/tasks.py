# tasks.py
from celery import Celery

# 初始化  app
app = Celery('tasks', backend='redis://localhost:6379/0',broker='pyamqp://admin:admin@127.0.0.1:5672//')
# app = Celery('tasks', broker='redis://localhost:6379/0')


@app.task   # 装饰器 包装成celery task
def add(x,y):
    return x + y
