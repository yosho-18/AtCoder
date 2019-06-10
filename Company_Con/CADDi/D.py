n = int(input())
d = []
for i in range(n):
    d.append(input())
# [d1, d2, d3, ..., dN]
d = [int(m) for m in d]#int型に直す
cnt = 0
for i in range(n):
    if d[i] % 2 == 0:
        cnt += 1
if cnt == n:
    print("second")
else:
    print("first")