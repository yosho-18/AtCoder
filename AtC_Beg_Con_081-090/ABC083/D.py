s = input()
n = len(s)
ans = n // 2
if n % 2 == 0:
    ans = n // 2
    for i in range(n // 2):
        if s[n // 2 - (i + 1)] != s[n // 2 + i]:
            break
        else:
            if s[n // 2 + i] == s[n // 2 + (i - 1)]:
                ans += 1
            else:
                break
else:
    ans += 1
    k = s[n // 2]
    for i in range(n // 2):
        if s[n // 2 - (i + 1)] != s[n // 2 + (i + 1)]:
            break
        else:
            if s[n // 2 + (i + 1)] == s[n // 2 + i]:
                ans += 1
            else:
                break
print(ans)