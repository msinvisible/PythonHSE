a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    if b > c:
        print(c, b, a)
    else:
        print(b, c, a)
elif b > a and b > c:
    if a > c:
        print(c, a, b)
    else:
        print(a, c, b)
elif c > a and c > b:
    if a > b:
        print(b, a, c)
    else:
        print(a, b, c)
elif a > b and a == c:
    print(b, a, c)
elif a > c and a == b:
    print(c, a, b)
else:
    print(a, b, c)
