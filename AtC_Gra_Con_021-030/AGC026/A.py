n = int(input())
a = [int(m) for m in input().split()]
ans = 0
tmp = 0
for i in range(1, n):
    if a[i - 1] == a[i]:
        tmp += 1
    else:
        tmp += 1
        ans += tmp // 2
        tmp = 0
tmp += 1
ans += tmp // 2
print(ans)