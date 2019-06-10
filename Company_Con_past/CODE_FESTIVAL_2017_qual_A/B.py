n, m, k = map(int, input().split())
gyoli = []
for i in range(n + 1):
  gyoli.append(i)
candiset = set()
for j in range(m + 1):
  for gyo in gyoli:
    candiset.add(gyo*j + (n-gyo)*(m-j))
if k in candiset:
  print("Yes")
else:
  print("No")
