N = int(input())
w = []
for i in range(N):
    w.append(input())
# [a1, a2, a3, ..., aN]
p = 0
for i in range(N):
    for j in range(i + 1, N):
        if w[i] == w[j]:
            p = 1
            break
v = []

for i in range(N):
    v.append([])

for j in range(N):
    for s in list(w[j]):
        v[j].append(s)

for k in range(N):
    if k != 0:
        if v[k - 1][len(v[k - 1]) - 1] != v[k][0]:
            p = 1
            break

if p == 0:
    print("Yes")
else:
    print("No")
