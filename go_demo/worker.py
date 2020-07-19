from celery import Celery

app = Celery(
    'worker',
    broker='redis://127.0.0.1:6379',
    backend='redis://127.0.0.1:6379',
)

app.conf.update(
    CELERY_TASK_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],  # Ignore other content
    CELERY_RESULT_SERIALIZER='json',
    CELERY_ENABLE_UTC=True,
    CELERY_TASK_PROTOCOL=1,  # 降级版本
)


@app.task
def add(a, b):
    return a + b


@app.task
def add_reflect(a, b):
    a+=1
    b+=1
    return a + b