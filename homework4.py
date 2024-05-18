immutable_var = 1, True, [1, 2, 3, 4]
print(immutable_var)
# immutable_var[0] = 2 при компеляции выдаёт ошибку
mutable_list = [1, 2, 3, 4, 5, 6]
mutable_list[:] = [23, 56, 75, 3214, 67]
print(mutable_list)