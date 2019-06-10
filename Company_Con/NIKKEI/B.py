n = int(input())
a = input()
b = input()
c = input()
cnt = 0
for i in range(n):
    if a[i] == b[i] and b[i] == c[i]:
        cnt += 2
    elif a[i] == b[i]:
        cnt += 1
    elif b[i] == c[i]:
        cnt += 1
    elif c[i] == a[i]:
        cnt += 1
    else:
        cnt += 0
print(2 * n - cnt)