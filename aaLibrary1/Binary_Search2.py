#単調性のある関数の解を見つける
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
#条件を満たす最小値（ng,ok）
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






#小数点を扱うときはこっち
def isOK(mid):
    if ((- a * mid + 100) - (b * math.sin(c * math.pi * mid))) > 0:
        return False
    elif ((- a * mid + 100) - (b * math.sin(c * math.pi * mid))) < 0:
        return True
    """else:
        return True"""


#汎用的な二分探索のテンプレ
def binary_search(ng, ok):
    #ng = -1 #「index = 0」が条件を満たすこともあるので、初期値は -1
    #ok = 10 ** 15 #「index = a.size()-1」が条件を満たさないこともあるので、初期値は a.size()
    cnt = 0
    #ok と ng のどちらが大きいかわからないことを考慮
    while cnt < 10 ** 5:#abs(ok - ng) > 10 ** (-1):
        mid = (ok + ng) / 2

        if isOK(mid):
            ok = mid
        else:
            ng = mid
        cnt += 1
    return ok










a = [1, 14, 32, 51, 51, 51, 243, 419, 750, 910]

#index が条件を満たすかどうか
def isOK(index, key):
    if a[index] >= key:
        return True
    else:
        return False

#汎用的な二分探索のテンプレ
def binary_search(key):
    ng = -1 #「index = 0」が条件を満たすこともあるので、初期値は -1
    ok = len(a) #「index = a.size()-1」が条件を満たさないこともあるので、初期値は a.size()

    #ok と ng のどちらが大きいかわからないことを考慮
    while abs(ok - ng) > 1:
        mid = (ok + ng) / 2

        if isOK(mid, key):
            ok = mid
        else:
            ng = mid
    return ok

def main():
    binary_search(51) #a[3] = 51 (さっきは 4 を返したが今回は「最小の index」なので 3)
    binary_search(1) #a[0] = 1
    binary_search(910) #a[9] = 910

    binary_search(52) # 6
    binary_search(0) #0
    binary_search(911) #10 (場外)


