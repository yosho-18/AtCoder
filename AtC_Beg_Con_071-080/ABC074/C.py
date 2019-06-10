a, b, c, d, e, f = map(int, input().split())

sug = 0
sugwat = 100 * a
for h in range(0,f + 1,100 * a):
    if h > f:
        break
    for i in range(0, f + 1, 100 * b):
        if h + i > f:
            break
        for j in range(0, f + 1, c):
            if h + i + j <= f:
                if h + i + j > 0:
                    if 100 * (j / (h + i + j)) > 100 * (e / (100 + e)):
                        break
            else:
                break
            for k in range(0, f + 1, d):
                if h + i + j + k <= f:
                    if h + i + j + k > 0:
                        if 100 * ((j + k) / (h + i + j + k)) <= 100 * (e / (100 + e)):
                            if 100 * (sug / sugwat) <= 100 * ((j + k) / (h + i + j + k)):
                                sugwat = h + i + j + k
                                sug = j + k
                else:
                    break

print(sugwat, sug)