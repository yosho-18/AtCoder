import sys
from collections import defaultdict
def wi(): return list(map(int, sys.stdin.readline().split()))
def i(): return int(sys.stdin.readline())
def mi(n): return [wi() for _ in range(n)]#MatrixInt

def main():
    n, q = wi()
    ab = mi(n - 1)
    px = mi(q)
    numdict = {}
    for i in range(n + 1):
        numdict[i] = []

    parli = [0] * (n + 1)
    parli[1] = 1
    for i in range(n - 1):
        if parli[ab[i][0]] == 0:
            parli[ab[i][0]] = 1
        else:
            numdict[ab[i][0]].append(ab[i][1])
        if parli[ab[i][1]] == 0:
            parli[ab[i][1]] = 1
        else:
            numdict[ab[i][1]].append(ab[i][0])

    plsdict = defaultdict(int)
    for i in range(q):
        plsdict[px[i][0]] += px[i][1]



    queue = []
    queue.append(1)
    while queue != []:
        po = queue.pop()
        for kk in numdict[po]:
            queue.append(kk)
            plsdict[kk] += plsdict[po]

    for i in range(1, n + 1):
        print(plsdict[i],"" , end="")

if __name__ == '__main__':
    main()