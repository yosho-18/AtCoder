s = input()
t = ""
for i in range(len(s)):
    if s[i] == "0":
        t += "0"
    elif s[i] == "1":
        t += "1"
    elif s[i] == "B":
        if len(t) != 0:
            k = list(t)
            del k[-1]

            t = ''.join(k)
            #t.pop(-1)
print(t)