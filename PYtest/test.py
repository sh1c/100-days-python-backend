import functools


def xs(func):
    @functools.wraps(func)
    def temp(*a):
        print("修饰器")

    return temp


@xs
def t(n):
    print(n)


t(0)
