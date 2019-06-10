n = int(input())
k = 0
count = 0
m = 0
for i in range(1, n + 1):
  count = 0
  j = i
  while j % 2 == 0:
    count += 1
    j = j // 2
  if i == 1:
    k = count
    m = i
  elif k < count:
    k = count
    m = i
print(m)
