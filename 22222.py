def decorator_a(func):
    print("我是外层a添加的第一个功能====")

    def wrapper():
        print("我是内层a添加的第一个功能****")
        func()
        print("我是内层a添加的第二个功能****")

    print("我是外层a添加的第二个功能====")
    return wrapper


def decorator_b(func):
    print("我是外层b添加的第一个功能&&&&")

    def wrapper():
        print("我是内层b添加的第一个功能####")
        func()
        print("我是内层b添加的第二个功能####")

    print("我是外层b添加的第二个功能&&&&")
    return wrapper


@decorator_b
@decorator_a
def test_a():
    print("我是原始函数")

