w, h= map(int, input().split())
for i in range(1, 10**5):
    if w == 4 * i and h == 3 * i:
        print("4:3")
        exit()
else:
    print("16:9")