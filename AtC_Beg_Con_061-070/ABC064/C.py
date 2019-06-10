n = int(input())
a = input().split()
a = [int(m) for m in a]
rate = {}
for i in range(9):
    rate[i] = 0
for i in range(n):
    for rank in range(9):
        if rank == 0:
            if 1 <= a[i] <= 400 * (rank + 1) - 1:
                rate[rank] += 1
        if rank == 8:
            if 400 * rank <= a[i]:
                rate[rank] += 1
        elif 400 * rank <= a[i] <= 400 * (rank + 1) - 1:
            rate[rank] += 1
maxco = 0
minco = 0
void = 0
for i in range(9):
    if rate[i] != 0:
        if i == 8:
            if void == 8:
                minco += 1
            maxco += rate[i]
        else:
            maxco += 1
            minco += 1
    else:
        void += 1
print(minco, maxco)