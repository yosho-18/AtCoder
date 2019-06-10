n, X = map(int, input().split())
x = input().split()
x = [int(m) for m in x]

z = x
z.append(X)
z.sort()

w = []

for i in range(n + 1):
    if i != 0:
        w.append(z[i] - z[i - 1])

n1=len(w)

#ユークリッド互除法の関数の定義
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)


if n1==1:
    print(w[0])
else:
    element = gcd(w[0], w[1])
    if n1==2:print(element)
    else:
        for i in range(2,n1):
            element=gcd(element,w[i])
        print(element)