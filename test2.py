"""def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = 10**9+7 #出力の制限
N = 10**10
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

a = cmb(10**9,80,mod)
print(a)"""
from collections import defaultdict
d = {}
d = defaultdict(int)
s = input()

# 文字別にカウント
for i in s:
    d[i] += 1
for k, v in d.items():
    print(k, v)

for ptn in itertools.combinations('MARCH',3):
    a,b,c = ptn
    ans += ctr[a] * ctr[b] * ctr[c]
print(ans)

import time

if __name__ == '__main__':
    start = time.time()
    p = 0
    for i in range(0,10**5):
        p += 1
    print(p)
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

