s = input()
alpha = "abcdefghijklmnopqrstuvwxyz"
tmpset = set()
n = len(s)
if n != 26:
    for i in range(n):
        tmpset.add(s[i])
    for i in range(26):
        if alpha[i] not in tmpset:
            s = s + alpha[i]
            print(s)
            exit()
else:
    if s == "zyxwvutsrqponmlkjihgfedcba":
        print(-1)
    else:
        for i in range(n - 1, 0, -1):
            if s[i] > s[i - 1]:
                tmpset.add(s[i])
                for j in range(26):
                    if alpha[j] in tmpset:
                        if s[i - 1] < alpha[j]:
                            s = s[:i - 1] + alpha[j]
                            print(s)
                            exit()
            else:
                tmpset.add(s[i])
