n = int(input())
result = list()
for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        if (n % (i + j) == 0) and ([i, j] not in result) and ([j, i] not in result) and (i != j):
            result.append([i, j])
for i in result:
    print(i[0], i[1], sep='', end='')

