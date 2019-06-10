n = int(input())
a = input().split()

a = [int(m) for m in a]

alicepoint = 0
bobpoint = 0

a.sort(reverse=True)

for i in range(n):
    if i % 2 == 0:
        alicepoint += a[i]
    else:
        bobpoint += a[i]

print(alicepoint - bobpoint)

