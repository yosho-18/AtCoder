n = int(input())
d = []
for i in range(n):
    d.append(input())
# [d1, d2, d3, ..., dN]
d = [int(m) for m in d]

d.sort()

count = 0

for j in range(n):
    if j == 0:
        count += 1
    elif d[j] != d[j-1]:
        count += 1

print(count)