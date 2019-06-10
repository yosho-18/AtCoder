n, m = map(int, input().split())
a = input().split()
a = [int(m) for m in a]
b = [0]
t = 0
for i in range(n):
    t += a[i]
    b.append(t)
