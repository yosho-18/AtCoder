s = input()
numberli = ["0","1","2","3","4","5","6","7","8","9"]
for i in range(len(s)):
    if s[i] in numberli:
        k = s[i]
        if i != len(s) - 1:
            if s[i + 1] in numberli:
                l = s[i + 1]
                print(k + l)
                exit()
            else:
                print(k)
                exit()
        else:
            print(k)
            exit()