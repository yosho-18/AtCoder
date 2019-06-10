from collections import deque
s = input()
ans = ""
n = len(s)
#parenthesis
bracketscnt = 0
signstack = deque()
for i in range(n):
    if s[i] == "+" or s[i] == "-" or s[i] == "*" or s[i] == "/":
        signstack.append(s[i])
    elif s[i] == "(":
        bracketscnt += 1
        ans += "("
    elif s[i] == ")":
        bracketscnt -= 1
        ans += ")"
        signstack.pop()
    elif s[i] == ",":
        ans += signstack[-1]
    else:
        ans += s[i]
print(ans)