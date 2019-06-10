n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

ar = [0]*n

for k in range(n):
  for j in range(n):
    if j <= k:
      ar[k] += x[j]
    if j >= k:
      ar[k] += y[j]
print(max(ar))
