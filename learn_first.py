from multiprocessing import Pool
import time

# 闭包
# def outer(num):
#     num += 2
#
#     def inner():
#         return num + 1
#
#     return inner
#
#
# fo = outer(3)
# c = fo()
# print(c)

# 装饰器
def showtime(func):
    def wrapper():
        time_start = time.time()
        func()
        time_end = time.time()
        print("函数运行一共花费了:{}".format(time_end - time_start))

    return wrapper


@showtime
def foo():
    print(111)
    time.sleep(2)


foo()

import time


def time_logger(flag=0):
    def showtime(func):
        def wrapper(a, b):
            start_time = time.time()
            func(a, b)
            end_time = time.time()
            print('spend is {}'.format(end_time - start_time))
            if flag:
                print('将此操作保留至日志')

        return wrapper

    return showtime


@time_logger(2)  # 得到闭包函数showtime,add = showtime(add)
def add(a, b):
    print(a + b)
    time.sleep(1)


add(3, 4)
