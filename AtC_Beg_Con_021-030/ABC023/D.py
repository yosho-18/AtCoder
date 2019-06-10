n = int(input())
hs = []
for i in range(n):#h:高さ
    hs.append([int(m) for m in input().split()])

a = [i for i in range(n)]

def isOK(mid):
    timeli = []
    for i1 in range(n):
        timeli.append((mid - hs[i1][0]) / hs[i1][1])
    timeli.sort()
    for j in range(n):
        if timeli[j] >= a[j]:
            pass
        else:
            return False
    else:
        return True

#汎用的な二分探索のテンプレ
def binary_search():
    ng = -1 #「index = 0」が条件を満たすこともあるので、初期値は -1
    ok = 10 ** 15 #「index = a.size()-1」が条件を満たさないこともあるので、初期値は a.size()

    #ok と ng のどちらが大きいかわからないことを考慮
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2

        if isOK(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(binary_search())