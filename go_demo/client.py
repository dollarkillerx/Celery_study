from worker import add, add_reflect
import time
from datetime import timedelta,datetime

# ar = add_reflect.apply_async(kwargs={'a': 1, 'b': 2}, serializer='json', expires=120)
# print('Result: {}'.format(ar.get()))

def register():
    start = time.time()
    result = add_reflect.apply_async(kwargs={'a': 1, 'b': 2}, serializer='json', expires=120)
    print("taskID: %s " % result.id)
    while True:
        if result.ready():
            try:
                print("result: ",result.get(timeout=1)) # 如果使用了后端存储 必须要调用get() or forget()来回收资源
            except:
                # 如果任务出现异常进行回滚
                result.traceback

            break



    print("耗时：%s 秒 " % (time.time() - start))

if __name__ == '__main__':
    register()