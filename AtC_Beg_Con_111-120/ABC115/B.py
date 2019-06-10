n = int(input())
d = []
for i in range(n):
    d.append(input())
# [d1, d2, d3, ..., dN]
d = [int(m) for m in d]#int型に直す
d.sort(reverse=True)
t = 0
for i in range(n):
    if i == 0:
        t += d[i]//2
    else:
        t += d[i]
print(t)