from tasks import add
import time

def register():
    start = time.time()
    result = add.delay(6,6)
    print("taskID: %s " % result.id)
    for i in range(100):
        if result.ready():
            try:
                print("result: ",result.get(timeout=1)  # 如果使用了后端存储 必须要调用get() or forget()来回收资源
            except:
                # 如果任务出现异常进行回滚
                result.traceback
            break

    print("耗时：%s 秒 " % (time.time() - start))

if __name__ == '__main__':
    register()