n = int(input())
s = []
t = []
for i in range(2 * n):#h:高さ
    if i <= n - 1:
        s.append([int(m) for m in input().split()])
    else:
        t.append([int(m) for m in input().split()])
for i in range(n):

