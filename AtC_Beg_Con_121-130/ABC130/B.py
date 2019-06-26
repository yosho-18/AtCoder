n, x = map(int, input().split())
L = [int(i) for i in input().split()]
ans = 1
d_i1 = 0
for i in range(n):
    d = d_i1 + L[i]
    if d <= x:
        ans += 1
    d_i1 = d
print(ans)