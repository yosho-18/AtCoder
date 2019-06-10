n = int(input())
a = input().split()
count = 0
p = 0

a = [int(m) for m in a]

while p != len(a):
    for i in range(n):
        if a[i] % 2 == 0:
            a[i] = a[i] / 2
            count += 1
        else:
            p += 1
    if p != len(a):
        p = 0

print(count)
