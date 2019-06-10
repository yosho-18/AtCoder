n = int(input())
d = []
for i in range(n):
    d.append(input())
# [d1, d2, d3, ..., dN]
d = [int(m) for m in d]#int型に直す
e = set(d)
print(len(e))