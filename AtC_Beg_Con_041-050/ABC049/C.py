s = input()
i = 0
n = len(s)
p = 0
while i < n:
    if i == 0:
        if s[i] == "d":
            if i + 5 <= n:
                if s[i:i+5] == "dream":
                    i = i + 5
                    if i + 5 < n:
                        if s[i] != "e" and s[i] != "d":
                            print("NO")
                            exit()
                else:
                    print("NO")
                    exit()
            else:
                print("NO")
                exit()
        elif s[i] == "e":
            if i + 2 <= n:
                if s[i:i+2] == "er":
                    i = i + 1
                else:
                    print("NO")
                    exit()
            else:
                print("NO")
                exit()
        else:
            print("NO")
            exit()
    else:
        if s[i] == "d":
            if i + 5 <= n:
                if s[i:i+5] == "dream":
                    i = i + 5
                    if i + 5 < n:
                        if s[i] != "e" and s[i] != "d":
                            print("NO")
                            exit()
                else:
                    print("NO")
                    exit()
            else:
                print("NO")
                exit()
        elif s[i] == "e":
            if i + 2 <= n:
                if s[i:i+2] == "er":
                    i = i + 1
                else:
                    print("NO")
                    exit()
            else:
                print("NO")
                exit()
        elif s[i] == "r":
            if s[i - 5: i + 1] == "eraser" and i - 5 >= 0:
                if s[i - 2] != "r":
                    if i + 1 < n:
                        if s[i + 1] == "d":
                            i = i + 1
                        elif s[i + 1] == "e":
                            i = i + 1
                        else:
                            print("NO")
                            exit()
                        #p = 1
                    else:
                        print("YES")
                        exit()
            elif i + 4 <= n:
                if s[i - 2] != "r":
                    if i + 1 < n:
                        if s[i + 1] == "d":
                            i = i + 1
                            p = 1
                        elif s[i + 1] == "e":
                            i = i + 1
                            p = 1
                    else:
                        print("YES")
                        exit()
                if s[i:i+4] == "rase":
                    i = i + 4
                    p = 1
                if p == 0:
                    print("NO")
                    exit()
            elif s[i - 2] != "r":
                if i + 1 < n:
                    if s[i + 1] == "d":
                        i = i + 1
                    elif s[i + 1] == "e":
                        i = i + 1
                    else:
                        print("NO")
                        exit()
                else:
                    print("YES")
                    exit()
            else:
                print("NO")
                exit()
        else:
            print("NO")
            exit()
    p = 0
print("YES")