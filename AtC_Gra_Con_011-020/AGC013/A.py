n = int(input())
a = [int(m) for m in input().split()]
ans = 1
vector = 0
for i in range(1, n):
    if i == 1:
        if a[i - 1] < a[i]:
            vector = 1
        elif a[i - 1] > a[i]:
            vector = -1
    else:
        if vector == 0:
            if a[i - 1] < a[i]:
                vector = 1
            elif a[i - 1] > a[i]:
                vector = -1
        elif vector == 1:
            if a[i - 1] > a[i]:
                vector = 0
                ans += 1
        elif vector == -1:
            if a[i - 1] < a[i]:
                vector = 0
                ans += 1
print(ans)