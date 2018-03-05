a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if a <= d and b <= e:
    print('YES')
elif a <= e and b <= d:
    print('YES')
elif b <= e and c <= d:
    print('YES')
elif b <= d and c <= e:
    print('YES')
elif c <= e and a <= d:
    print('YES')
elif c <= d and a <= e:
    print('YES')
else:
    print('NO')
