n = int(input())
a = [int(m) for m in input().split()]

ansli = []
for k in range(1, n + 1):
    fstsum = sum(a[:k])
    ansli.append(fstsum)
    j = 0
    for i in range(k, n):
        fstsum = -a[j] + fstsum + a[i]
        ansli.append(fstsum)
        j += 1
    print(max(ansli))
    ansli = []