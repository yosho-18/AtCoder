n = int(input())
l0 = 2
l1 = 1
s = 0
for i in range(n - 1):
  s = l0 + l1
  l0 = l1
  l1 = s

if n == 1:
  print(l1)
else:
  print(s)
