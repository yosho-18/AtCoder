n = int(input())
s1 = input()
s2 = input()
mod = 10 ** 9 + 7
count = 1
p = 0
for i in range(n):
    if i == 0:
        if s1[i] == s2[i]:
            count *= 3
        else:
            count *= 6
            p = 1
    elif p == 0:
        if s1[i - 1] == s2[i - 1] and s1[i] != s2[i]:
            count *= 2
            p = 1
        elif s1[i - 1] == s2[i - 1] and s1[i] == s2[i]:
            count *= 2
        elif s1[i - 1] != s2[i - 1] and s1[i] == s2[i]:
            count *= 1
        elif s1[i - 1] != s2[i - 1] and s1[i] != s2[i]:
            count *= 3
            p = 1
    elif p == 1:
        p = 0
print(count % mod)