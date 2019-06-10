n = int(input())
a = [int(m) for m in input().split()]
pair = []
for i in range(n):
  pair.append([i + 1, a[i]])

for i in range(n):
  pair[i].sort()
tuplepair = []
for i in range(n):
  tuplepair.append((pair[i][0], pair[i][1]))
print(n - len(set(tuplepair)))
