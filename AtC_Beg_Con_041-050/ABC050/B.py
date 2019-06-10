n = int(input())
a = input().split()
t = [int(m) for m in a]
m = int(input())
#行列
c = []
for i in range(m):#h:高さ
    c.append([int(m) for m in input().split()])
k = sum(t)
for i in range(m):
    print(k - t[c[i][0] - 1] + c[i][1])