n = int(input())
a = input().split()
a = [int(m) for m in a]

a.sort()
sym = 0
symc = 0
delc = 0
for i in range(n):
    if i == 0 and n == 1:
        if a[i] == 1:
            delc = 0
        else:
            delc = 1
    elif i == 0:
        sym = a[i]
        symc += 1
    elif a[i] != a[i - 1]:
        if symc < a[i - 1]:
            delc += symc
        elif symc > a[i - 1]:
            delc += symc - a[i - 1]
        sym = a[i]
        symc = 1
        if i == n - 1:
            if symc < a[i]:
                delc += symc
            elif symc > a[i]:
                delc += symc - a[i]
    elif i == n - 1:
        symc += 1
        if symc < a[i]:
            delc += symc
        elif symc > a[i]:
            delc += symc - a[i]
    else:
        symc += 1

print(delc)