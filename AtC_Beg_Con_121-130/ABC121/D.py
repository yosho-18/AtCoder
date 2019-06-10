a, b = map(int, input().split())
"""s = bin(a)
t = bin(b)
s = s[2:]
t = t[2:]
cri = len(t)
s = (cri - len(s)) * "0" + s
q = 0
for i in reversed(range(len(s))):
    if i == len(s) - 1:"""
#F(A, B) = F(0, A − 1) ⊕ F(0, B),なぜなら n ⊕ n = 0
#任意の偶数 n について n ⊕ (n + 1) = 1

def F(x):
    if x == -1:
        return 0
    elif x % 2 == 1:
        if (x + 1) % 4 == 0:
            return 0
        else:
            return 1
    else:
        if x % 4 == 0:
            return x
        else:
            return 1 ^ x

ans = F(b) ^ F(a - 1)

print(ans)