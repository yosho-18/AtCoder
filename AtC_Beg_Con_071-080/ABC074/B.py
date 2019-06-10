n = int(input())
k = int(input())
x = list(map(int, input().split()))
dis = 0
for i in range(n):
  dis += 2 * min(abs(x[i]),abs(x[i] - k))
print(dis)
