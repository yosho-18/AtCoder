k, t = map(int, input().split())
a = [[int(m), 0] for m in input().split()]
prohibit = 1
ans = 0
if t == 1:
    ans = a[0][0] - 1
else:
    for i in range(k):
        a.sort(reverse=True)
        if a[1][0] == 0:
            ans = a[0][0] - 1
            break
        else:
            if i == 0:
                a[1][1] = 1
            if a[0][1] == 0:
                a[0][0] -= 1
                a[0][1] = 1
                prohibit = 0
            elif a[1][1] == 0:
                a[1][0] -= 1
                a[1][1] = 1
                prohibit = 1
            for j in range(t):
                if prohibit != j:
                    a[j][1] = 0
print(ans)