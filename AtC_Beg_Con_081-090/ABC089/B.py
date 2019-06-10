n = int(input())
a = input().split()
a = [str(m) for m in a]

for i in a:
    if i == "Y":
        print("Four")
        exit()

print("Three")