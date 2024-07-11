import decimal


def add_everything_up(a, b):
    try:
        a + b
    except TypeError as exc:
        result = str(a) + str(b)
    else:
        result = decimal.Decimal(str(a)) + decimal.Decimal(str(b))
    finally:
        return result


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
