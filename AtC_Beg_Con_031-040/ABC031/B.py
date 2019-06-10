l, h = map(int, input().split())
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

for i in range(n):
    if l <= a[i] <= h:
        print(0)
    elif a[i] < l:
        print(l - a[i])
    elif h < a[i]:
        print(-1)