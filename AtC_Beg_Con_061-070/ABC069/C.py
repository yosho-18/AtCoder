n = int(input())
a = list(map(int, input().split()))
c4 = 0
c2 = 0
for i in range(n):
    if a[i] % 4 == 0:
        c4 += 1
    elif a[i] % 2 == 0:
        c2 += 1

d4 = n // 2
d2 = 0
if n % 2 == 0:
    if c4 >= n // 2:
        print("Yes")
        exit()
    else:
        for i in range(n // 2):
            if i == 0:
                d4 -= 1
                d2 += 2
            elif i == n // 2 - 1:
                d4 -= 1
                d2 += 2
            else:
                d4 -= 1
                d2 += 2
            if c4 >= d4 and c2 >= d2:
                print("Yes")
                exit()
else:
    if c4 >= n // 2:
        print("Yes")
        exit()
    else:
        for i in range(n // 2):
            if i == 0:
                d4 -= 1
                d2 += 3
            elif i == n // 2 - 1:
                d4 -= 1
                d2 += 2
            else:
                d4 -= 1
                d2 += 2
            if c4 >= d4 and c2 >= d2:
                print("Yes")
                exit()
print("No")