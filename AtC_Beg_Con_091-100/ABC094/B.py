n,m,x = map(int, input().split())
a = [int(y) for y in input().split()]

c1 = 0
c2 = 0

for i in range(1, x):
  if i in a:
    c1 += 1

for i in range(x + 1, n):
  if i in a:
    c2 += 1

print(min(c1,c2))
