a = int(input())
b = int(input())
c = int(input())
d = 0
if a == b:
    d += 2
if a == c:
    if d > 0:
        d += 1
    else:
        d += 2
print(d)


