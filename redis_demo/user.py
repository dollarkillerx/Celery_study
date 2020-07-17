from tasks import send_msg
import time

def register():
    start = time.time()
    send_msg.delay("Hello World")
    print("耗时：%s 秒 " % (time.time() - start))

if __name__ == '__main__':
    register()