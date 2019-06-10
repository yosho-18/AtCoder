n = int(input())
a = [int(m) for m in input().split()]
S = 0
for i in range(n):
    S += abs(a[i])
fu = 0
minabs = float("INF")
for i in range(n):
    if a[i] < 0:
        fu += 1
    minabs = min(minabs, abs(a[i]))

if n % 2 == 0:
    if fu % 2 == 0:
        print(S)
    else:
        print(S - 2 * minabs)
else:
    if fu % 2 == 0:
        print(S)
    else:
        print(S - 2 * minabs)