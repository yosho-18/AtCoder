import itertools
n = int(input())
a = [int(m) for m in input().split()]
a.sort()
acculi = list(itertools.accumulate(a))
sym = -1
for i in range(n - 1):
    if 2 * acculi[i] < a[i + 1]:
        sym = i
print(n - sym - 1)