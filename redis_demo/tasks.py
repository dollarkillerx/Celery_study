# tasks.py
from celery import Celery

# 初始化  app
app = Celery('tasks', broker='redis://localhost:6379/0')


@app.task
def send_msg(msg):
    print("get Message ", msg)
    return "success"

