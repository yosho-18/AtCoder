n = int(input())
a = input().split()
a = [int(m) for m in a]
b = sum(a) / n
bli = []
for i in range(n):
    bli.append([abs(b - a[i]), i])
bli.sort()
print(bli[0][1])