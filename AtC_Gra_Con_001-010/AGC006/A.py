n = int(input())
s = input()
t = input()
ans = n
for i in range(n):
    for j in range(n):
        if s[i + j] == t[j]:
            if i + j == n - 1:
                print(ans)
                exit()
        else:
            ans += 1
            break
print(2 * n)