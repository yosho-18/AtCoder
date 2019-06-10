n = int(input())
k = int(input())
c = 1
for i in range(n):
    if c * 2 < c + k:
        c = c * 2
    else:
        c = c + k
print(c)
