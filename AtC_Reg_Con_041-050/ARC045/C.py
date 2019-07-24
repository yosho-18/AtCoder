import sys
import numpy as np


def wi(): return list(map(int, sys.stdin.readline().split()))


def mi(n): return [wi() for _ in range(n)]  # MatrixInt


N, M = wi()
room_range = mi(M)

X = np.zeros(N)
for rr in room_range:
    X[rr[0] - 1:rr[1]] += 1
X = np.array([2 if x >= 2 else 1 for x in X])
good_range = []
for m, rr in enumerate(room_range):
    if sum(X[rr[0] - 1:rr[1]]) == 2 * (rr[1] - rr[0] + 1):
        good_range.append(m + 1)
print(len(good_range))
for i in good_range:
    print(i)
