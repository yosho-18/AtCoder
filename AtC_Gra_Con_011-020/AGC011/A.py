#横にn個入力
n, c, k = map(int, input().split())
d = []
for i in range(n):
    d.append(input())
# [d1, d2, d3, ..., dN]
t = [int(m) for m in d]#int型に直す

t.sort()
current = 0
ans = 0
psn = 0
getonpsn = 0
for i in range(n):
    psn += 1
    if i == 0:
        current = t[i]
    if t[i] - current > k:
        psn -= 1
        ans += psn // c
        getonpsn += (psn // c) * c
        if psn // c == 0:
            getonpsn += psn
            ans += 1
            psn = 0
            #if getonpsn != n:
            current = t[getonpsn]
            if i == n - 1:
                    ans += 1
        elif getonpsn != n:#iminai
            current = t[getonpsn]
            if i == n - 1:
                if t[i] - current > k:
                    ans += 2
                else:
                    ans += 1

        psn = psn % c


        psn += 1
    elif i == n - 1:
        ans += (psn + c + 1) // c


print(ans)