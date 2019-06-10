s = input()
t = "keyence"
if t in s:
    print("YES")
    exit()
if len(s) >= 7:
    if "k" in s and "eyence" in s:
        if s[0] == "k" and s[-1] == "e" and s[-2] == "c" and s[-3] == "n" and s[-4] == "e" and s[-5] == "y" and s[-6] == "e":
            print("YES")
            exit()
    if "ke" in s and "yence" in s:
        if s[0] == "k" and s[-1] == "e" and s[-2] == "c" and s[-3] == "n" and s[-4] == "e" and s[-5] == "y" and s[1] == "e":
            print("YES")
            exit()
    if "key" in s and "ence" in s:
        if s[0] == "k" and s[-1] == "e" and s[-2] == "c" and s[-3] == "n" and s[-4] == "e" and s[2] == "y" and s[1] == "e":
            print("YES")
            exit()
    if "keye" in s and "nce" in s:
        if s[0] == "k" and s[-1] == "e" and s[-2] == "c" and s[-3] == "n" and s[3] == "e" and s[2] == "y" and s[1] == "e":
            print("YES")
            exit()
    if "keyen" in s and "ce" in s:
        if s[0] == "k" and s[-1] == "e" and s[-2] == "c" and s[4] == "n" and s[3] == "e" and s[2] == "y" and s[1] == "e":
            print("YES")
            exit()
    if "keyenc" in s and "e" in s:
        if s[0] == "k" and s[-1] == "e" and s[5] == "c" and s[4] == "n" and s[3] == "e" and s[2] == "y" and s[1] == "e":
            print("YES")
            exit()
print("NO")
