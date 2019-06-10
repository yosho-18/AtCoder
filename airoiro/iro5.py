import itertools
nums = [1, 2, 3]
for balls in itertools.permutations(nums, 2):
    print(balls)
"""(1, 2)
(1, 3)
(2, 1)
(2, 3)
(3, 1)
(3, 2)"""
nums = [1, 2, 3]
for balls in itertools.combinations(nums, 2):
    print(balls)
"""(1, 2)
(1, 3)
(2, 3)"""
nums = [1, 2, 3]
for balls in itertools.product(nums, repeat=2):#3**2
    print(balls)
"""(1, 1)
(1, 2)
(1, 3)
(2, 1)
(2, 2)
(2, 3)
(3, 1)
(3, 2)
(3, 3)"""
nums = [1, 2, 3]
for balls in itertools.combinations_with_replacement(nums, 2):
    print(balls)
"""(1, 1)
(1, 2)
(1, 3)
(2, 2)
(2, 3)
(3, 3)"""
signs = ['a', 'b', 'c']
nums = [1, 2, 3]
for pairs in itertools.product(signs, nums):
    print(pairs)
"""('a', 1)
('a', 2)
('a', 3)
('b', 1)
('b', 2)
('b', 3)
('c', 1)
('c', 2)
('c', 3)"""

#多次元配列
#?AGC,?ACG,A?GC,AG?C,?GAC
A, G, C, T = 0, 1, 2, 3
#[[[],[]],]
#dp[i][A][T][C] += dp[i - 1][][][]
dp = [[] for i in range(n + 1)]
for i in range(n + 1):
    for j in range(4):
        dp[i].append([])
for i in range(n + 1):
    for j in range(4):
        for k in range(4):
            dp[i][j].append([])
for i in range(n + 1):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                dp[i][j][k].append(0)
dp[0][T][T][T] = 1

import sys
sys.setrecursionlimit(10**7)