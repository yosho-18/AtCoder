s = input()
k = int(input())
ansset = set()
n = len(s)
if n < k:
    print(0)
else:
    for i in range(n - k + 1):
        st = s[i:k + i]
        ansset.add(st)
    print(len(ansset))