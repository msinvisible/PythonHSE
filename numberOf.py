p = -1
c = 0
m = 0
e = int(input())
while e != 0:
    if p == e:
        c += 1
    else:
        p = e
        m = max(m, c)
        c = 1
    e = int(input())
m = max(m, c)
print(m)
