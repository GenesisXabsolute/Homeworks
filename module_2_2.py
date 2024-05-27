a = int(input())
b = int(input())
c = int(input())
d = 0
if a == b == c:
    d = 3
elif a == b or a == c or b == c:
    d = 2
print(d)


