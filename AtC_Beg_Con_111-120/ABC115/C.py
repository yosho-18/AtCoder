n, k = map(int, input().split())
d = []
for i in range(n):
    d.append(input())
# [d1, d2, d3, ..., dN]
h = [int(m) for m in d]#int型に直す
h.sort(reverse=True)
li = []
for i in range(n):
    if i + k <= n:
        li.append(h[i] - h[i + k - 1])
    else:
        break
print(min(li))