n = int(input())
d,x = map(int, input().split())
a = [int(input()) for i in range(n)]
co = 0
for i in range(1, d + 1):
  for j in a:
    for k in range(d + 1):
      if i ==  k * j + 1:
        co += 1
co += x
print(co)
