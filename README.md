# Celery Study
Celery Python实现分布式[队列]服务 支持即时任务&定时任务

## 多语言
可以通过暴露 HTTP 的方式进行，任务交互以及其它语言的集成开发。
- [Node.js](https://github.com/mher/node-celery) 已停止维护   【非官方】
- [Php](https://github.com/gjedeer/celery-php)                【非官方】
- [GO](https://github.com/gocelery/gocelery)                  【非官方】 

## 5大金刚
- Task
    - 字面意思任务
- Broker
    - 队列
    - Celery 本身不提供队列服务，一般用 Redis 或者 RabbitMQ 来扮演 Broker 的角色
- Worker
    - 消费者
- Beat
    - 定时调度器  (cron定时发给Broker)
- Backend
    - 保存任务的执行结果
    - 执行成功OR失败  

![Backend](./README/584bbf78e1783.png)

### 以redis 为 Broker 示例  redis_demo
- install `pip3 install -U "celery[redis]"`
```python3
# tasks.py
from celery import Celery

# 初始化  app
app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task    # 函数用app.task 装饰器修饰之后，就会成为Celery中的一个Task。
def send_msg(msg):
    print("get Message ", msg)
    return "success" 
```
- 启动worker
    - `celery -A tasks worker --loglevel=info` 
    - -A： 指定 celery 实例在哪个模块中

    