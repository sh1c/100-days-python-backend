import functools
import random
import time


def timer(func):
    @functools.wraps(func)
    def warp(*args):
        t = time.perf_counter()
        result = func(*args)
        spend = time.perf_counter() - t
        print(f"time:{spend}")
        return result

    return warp


@timer
def loop(n):
    while True:
        if random.random() > 0.99:
            break
    print(n * 10)


loop(1)
