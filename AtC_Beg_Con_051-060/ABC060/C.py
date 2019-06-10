n,t = map(int, input().split())
a = input().split()
a = [int(m) for m in a]
X = 0

for i in range(n):
    if i == 0:
        u = a[0]
        if n == 1:
            X += t
            break
        else:
            v = a[1]
    if u + t < v:
        X += t
    else:
        X += v - u
    u = v
    if i + 1 < n:
        v = a[i + 1]
    if i == n - 1:
        X += t
print(X)