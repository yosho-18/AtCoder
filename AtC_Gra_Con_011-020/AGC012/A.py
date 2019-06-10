n = int(input())
a = [int(i) for i in input().split()]
a.sort()
ans = 0
for i in range(n, 3 * n, 2):
  ans += a[i]
print(ans)
