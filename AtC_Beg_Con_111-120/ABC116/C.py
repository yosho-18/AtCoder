n = int(input())
h = [int(m) for m in input().split()]
ans = 0
k = 1
tmp = -1
stmp = 0
numtmp = float("INF")
p = 0
while True:
    if k == 1:
        ans += min(h)
        t = min(h)
        for i in range(n):
            h[i] = h[i] - t
    else:
        for i in range(tmp + 1, n):
            p = 0
            if h[i] != 0:
                numtmp = min(numtmp, h[i])
                if numtmp == h[i]:
                    tmp = i
            else:
                tmp = i
                if numtmp != float("INF"):
                    ans += numtmp
                for j in range(stmp, tmp):
                    h[j] = h[j] - numtmp
                stmp = tmp + 1
                numtmp = float("INF")
                p = 1
            if i == n - 1 and p != 1:
                tmp = i + 1
                if numtmp != float("INF"):
                    ans += numtmp
                for j in range(stmp, tmp):
                    h[j] = h[j] - numtmp
                stmp = tmp + 1
                numtmp = float("INF")
                p = 1
    p = 0
    k += 1
    tmp = -1
    stmp = 0
    numtmp = float("INF")
    for i in range(n):
        if h[i] != 0:
            break
        if h[i] == 0:
            if i == n - 1:
                print(ans)
                exit()