n = int(input())
t, a = map(int, input().split())
h = [int(m) for m in input().split()]
ar = []
for j in range(n):
    ar.append(abs(t - h[j] * 0.006 - a))

co = ar.index(min(ar)) + 1
print(co)