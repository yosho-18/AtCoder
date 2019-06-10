n = int(input())
p = list(map(int, input().split()))
swapcount = 0
for i in range(n):
    if i != n - 1:
        if p[i] == i + 1:
            k = p[i + 1]
            p[i + 1] = p[i]
            p[i] = k
            swapcount += 1
    else:
        if p[i] == i + 1:
            swapcount += 1

print(swapcount)