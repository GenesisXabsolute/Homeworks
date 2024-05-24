def test(*args):
    print(*args)


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


