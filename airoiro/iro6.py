from collections import deque
signstack = deque()
signstack.pop()

from heapq import heappush, heappop, heappushpop
notfirst =[]
heappush(notfirst, f[i][1])
# デフォルトでは最小値を返すので，マイナスをつけて最大値を返すようにする
donyoku -= heappop(notfirst)

heappushpop(heap, item)  # pushしてpopする

import itertools
accua = list(itertools.accumulate(a))

import bisect
a = [1, 2, 3, 5, 6, 7, 8, 9]
bisect.bisect_left(a, 4)#挿入するindexを返す（挿入はしない）
>>> 3
bisect.bisect_left(a, 5)#同じ値があるときにどちらに置くか
>>> 3
bisect.bisect_right(a, 5)
>>> 4
# 4は入ってません
# 左側
bisect.insort_left(a, 4)
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9]

# 右側
bisect.insort_right(a, 5)
>>> a
[1, 2, 3, 4, 5, 5, 6, 7, 8, 9]


bi = [0,0,0,1,1,0,0,0,1,1,0,1]
gr = itertools.groupby(bi)
for key, group in gr:
    print(f'{key}: {list(group)}')

# 0: [0, 0, 0]
# 1: [1, 1]
# 0: [0, 0, 0]
# 1: [1, 1]
# 0: [0]
# 1: [1]

total = sum(map(int, list(str(A)))) + sum(map(int, list(str(B))))

import random

l = [0, 1, 2, 3, 4]

print(random.choice(l))