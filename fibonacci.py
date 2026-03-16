def fibonacci(n):
    """生成斐波那契数列的前n个数"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib


def fibonacci_recursive(n):
    """递归方式计算第n个斐波那契数"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibonacci_generator(n):
    """生成器方式生成斐波那契数列"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    n = 10
    print(f"斐波那契数列前{n}个数: {fibonacci(n)}")
    print(f"第{n}个斐波那契数(递归): {fibonacci_recursive(n)}")
    print(f"斐波那契数列(生成器): {list(fibonacci_generator(n))}")
