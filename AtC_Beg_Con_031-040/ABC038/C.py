n = int(input())
a = [int(m) for m in input().split()]
b = [0] * n
for i in range(n - 1):
    if a[i] >= a[i + 1]:
        b[i] = -1
b[n - 1] = -1
ans = 0
pre = -1
for i in range(n):
    if b[i] == -1:
        if pre == -1:
            ans += (i + 1) * (i + 2) // 2
        else:
            ans += (i - pre) * (i + 1 - pre) // 2 # - (pre + 1) * (pre + 2) // 2
        pre = i
print(ans)
