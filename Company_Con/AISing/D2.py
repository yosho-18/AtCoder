import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))
X = [int(input()) for i in range(Q)]
A.reverse()

cums = [0]
cums_e = [0]
for i, a in enumerate(A):
    cums.append(cums[-1] + a)
    cums_e.append(cums_e[-1] + (0 if i % 2 else a))

borders = []
scores = []
for i in range(1, N // 2 + N % 2):
    b = (A[i] + A[2 * i]) // 2 + 1
    borders.append(b)
    s = cums[i] + cums_e[-1] - cums_e[2 * i]
    scores.append(s)
if N % 2:
    scores.append(cums[N // 2 + 1])
else:
    scores.append(cums[N // 2])

borders.reverse()
scores.reverse()

ans = []
for x in X:
    i = bisect.bisect(borders, x)
    ans.append(scores[i])
print(*ans, sep='\n')
