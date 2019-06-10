s = input()
for i in range(1, len(s)):
    s = s[:-1]
    if len(s) % 2 == 0:
        t = s[:len(s) // 2]
        u = s[len(s) // 2:]
        if t == u:
            print(len(s))
            exit()