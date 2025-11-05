import queue
import threading
import time

q = queue.Queue(maxsize=5)


def pro():
    for i in range(10):
        q.put(f"食物{i}")
        print(f"做了食物{i}")
        time.sleep(0.2)


def cons():
    for i in range(10):
        q.get(f"食物{i}")
        print(f"吃了食物{i}")
        time.sleep(0.2)


threading.Thread(target=pro, daemon=True).start()
threading.Thread(target=cons, daemon=True).start()


time.sleep(10)
