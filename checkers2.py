x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 != x2 and y1 != y2 and y2 <= 8 and x2 <= 8 and y2 > y1:
    if (x2-x1+y2-y1) % 2 == 0 and y2-y1 >= abs(x2-x1):
        print("YES")
    else:
        print('NO')
else:
    print("NO")
