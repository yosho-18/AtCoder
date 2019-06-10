n = int(input())
v = [int(m) for m in input().split()]
c = [int(m) for m in input().split()]
ans = 0
for i in range(n):
    if v[i] - c[i] >= 0:
        ans += v[i] - c[i]
print(ans)