n, k = map(int, input().split())
a = input().split()
a = [int(m) for m in a]
a.sort(reverse=True)
length = 0
for i in range(k):
    length += a[i]
print(length)