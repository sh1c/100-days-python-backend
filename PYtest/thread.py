import multiprocessing
import threading
import time

worker = 4
data = 10**7


def counter(n):
    for i in range(n):
        i = 3.14159 * 2.71828**2


def treadings():
    treads = [threading.Thread(target=counter, args=(data,)) for i in range(worker)]
    start = time.perf_counter()
    for i in treads:
        i.start()
    for i in treads:
        i.join()

    return time.perf_counter() - start


def processings():
    with multiprocessing.Pool(worker) as p:  # 开四个池子不用with进程不会消失
        # 把列表里的每一个元素当成一个任务，依次派给进程池里空闲的子进程
        start = time.perf_counter()
        p.map(counter, [data] * worker)
        return time.perf_counter() - start


if __name__ == "__main__":
    print(f"线程用时:{treadings():0.2f}")
    print(f"进程用时:{processings():0.2f}")
