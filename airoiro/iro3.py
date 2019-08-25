#list*
li1 = [1, 3, 5]
li2 = [2, 4, 6]
combined1 = [x * y for (x, y) in zip(li1, li2)]
# => [2, 12, 30]
#リスト内峰表記
S=[abs(A-(T-H[i]*0.006)) for i in range(N)]
TEMP = [(abs((T - H[i] * 0.006) - A), i + 1) for i in range(N)]
print(min(TEMP)[1])
PY = [list(map(int, input().split())) + [i] for i in range(M)]
#for
for p, y, i in PY:#RY = [[dascs,vcs,asc],[acsac,vd,vd],..]

#enumerate
for i, name in enumerate(l, 1):
    print('{:03}_{}'.format(i, name))
# 001_Alice
# 002_Bob
# 003_Charlie

#zip
names = ['Alice', 'Bob', 'Charlie', 'Dave']
ages = [24, 50, 18]

for name, age in zip(names, ages):
    print(name, age)
# Alice 24
# Bob 50
# Charlie 18

# zip_longest
from itertools import zip_longest
names = ['Alice', 'Bob', 'Charlie', 'Dave']
ages = [24, 50, 18]
points = [100, 85]

for name, age, point in zip_longest(names, ages, points, fillvalue=20):
    print(name, age, point)
# Alice 24 100
# Bob 50 85
# Charlie 18 20
# Dave 20 20


#同じ要素のリスト
n = 8
a = [0] * n
print(a)#[0, 0, 0, 0, 0, 0, 0, 0]
[None]*n #kara


#空二重リスト
D = [[] for i in range(n)]

#
cnt = {k: [] for k in range(n + 1)}

#1*10^9
1e9

#print if else
print('TLE' if ans == 1003 else ans)

#//切捨て、int(-n/111)と同じ
-n//111#-112//111 == -2

#mathモジュール
import math
math.ceil(x)

#set()
a = [12,23,34,12]
b = str(191)
p = set(a)#{12,34,23}重複しない
b2 = set(b)#{9,1}
q = list(p)#[12,34,23]

#プログラムを終了する
exit()

#真偽
0,1
"","egvf"
[],[egvrf]

#最後のリストの要素
w[-1]
#dd
from collections import defaultdict

d = defaultdict(int)
d = defaultdict(lambda: float("INF"))
s = "abrakadabra"

# 文字別にカウント
for i in s:
    d[i] += 1
#Counter
import collections

l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']
c = collections.Counter(l)

print(c)
# Counter({'a': 4, 'c': 2, 'b': 1})
d = {}
for i in c:
    if c[i] >= 2:
        d[i] = c[i]
c.keys()
col.values()[i]
c.items()

if d != {}:
    dct = sorted(d.items(), key=lambda x: -x[0])#keyの降順に並べ替え
if al not in c:#このkeyが辞書にあるかの判定
#アルファベット、数字
alpha = "abcdefghijklmnopqrstuvwxyz"
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha = [chr(i) for i in range(ord('a'), ord('z')+1)]
[chr(i) for i in range(ord('A'), ord('Z')+1)]
[chr(i) for i in range(ord('0'), ord('9')+1)]
def SS(n):
    return sum(int(i) for i in str(n))

#リストをくっつける
t.append( ''.join(s[i]))
print(''.join(s[i]), end="")

#改行しない、空白なし
print(a[i][j], end = '')
print(s,sep='')
print()#改行

l_n_str = [int(n) for n in strli]
ss = [s_ for idx, s_ in enumerate(list(s)) if idx % 2 == 0]
print(''.join(ss))
['Odd','Even'][a*b%2==0]
5.1 % 1 = 0.09999999999999964
input().replace("2017", "2018")
s = ''.join(s)
" ".join(map(str, ansli[i]))
src = [int(input()) for i in range(N)]
ctr = Counter(src)
print(len(ctr.items()))
input().count("9") > 0
s.remove(x)
s.add(x)

"%06d%06d" %
buf[i] = '{:06d}{:06d}'.format(p, j + 1)
print('\n'.join(buf))
"{:012d}".format(v)
for k, (y, j) in enumerate(d):
        ans[j] = "%06d%06d" % (i+1, k+1)
print(*ans, sep='\n')
ans = zip(*[i for i in zip(*a) if '#' in i])



print(d.get('key1'))
# val1

print(d.get('key5'))
# None
#source: dict_get.py
#None以外の値を返したい場合は、第二引数にキーが存在しない場合に返すデフォルト値を指定する。

print(d.get('key5', 'NO KEY'))
# NO KEY

print(d.get('key5', 100))
# 100

functools.reduce(lambda a, b: a + b, overfiveli2)