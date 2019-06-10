s = input()
if int(s[:4]) >= 2019:
    if int(s[5:7]) >= 5:
        print("TBD")
    else:
        print("Heisei")
else:
    print("Heisei")