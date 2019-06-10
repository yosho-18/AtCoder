n = int(input())

def g(k, l):
    if l == 0:
        if k == 0:
            return 0
        elif k == 1:
            return 1
        else:
            return 10 ** (k - 1) + 9 * g(k - 1, 0) + g(k - 1, 0)
    if l == 1:
        return g(k, 0) + 1
    elif k >= 1:
        return 10 ** k + l * g(k, 0)
    #elif k == 1:
        #return l * g(k, 1)
    elif k == 0:
        if l == 0:
            return 0
        else:
            return 1
numli = []
cpn = n
for i in range(1, len(str(cpn)) + 1):
    numli.append(n % 10 ** i)
    n -= n % 10 ** i

ans = 0
cnt1 = 0
for i in range(1, len(str(cpn)) + 1):
    if numli[-i] != 0:
        ans += g(len(str(cpn)) - i, int(str(numli[-i])[0]))
        ans += numli[-i] * cnt1
        if int(str(numli[-i])[0]) == 1:
            cnt1 += 1



print(ans)