import sys
from collections import deque


def main():
    input = sys.stdin.readline
    n, q = map(int, input().split())

    edge = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1;
        v -= 1
        edge[u].append(v)

    cost = [0] * n
    for _ in range(q):
        p, x = map(int, input().split())
        p -= 1
        cost[p] += x

    for idx, e in enumerate(cost):
        if e == 0: continue
        for f in edge[idx]:
            cost[f] += e

    print(*cost)


if __name__ == "__main__":
    main()
