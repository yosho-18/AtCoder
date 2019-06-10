s = input()
k = int(input())
n = len(s)
mod = 26
alpha = "abcdefghijklmnopqrstuvwxyz"
aldic = {}
ansstr = ""
for i, al in enumerate(alpha, 1):
    aldic[al] = i

for i in range(n - 1):
    if k >= mod - aldic[s[i]] + 1 and s[i] != "a":
        ansstr += "a"
        k -= mod - aldic[s[i]] + 1
    else:
        ansstr += s[i]
ansstr += alpha[(aldic[s[n - 1]] + k - 1) % mod]
print(ansstr)


