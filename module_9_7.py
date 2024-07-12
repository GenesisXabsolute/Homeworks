def is_prime(func):
    def wrapper(a, b, c):
        summa = a + b + c
        if all([(summa % i) != 0 for i in range(2, summa)]):
            print('Простое')
        else:
            print('Составное')
        res = func(a, b, c)
        return res
    return wrapper


@is_prime
def sum_three(a, b, c):
    d = a + b + c
    return d


result = sum_three(2, 3, 6)
print(result)
