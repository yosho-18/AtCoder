#横にn個入力
a, b = map(int, input().split())
if a % 3 == 0:
    print("Possible")
    exit()
elif b % 3 == 0:
    print("Possible")
    exit()
elif (a + b) % 3 == 0:
    print("Possible")
    exit()
print("Impossible")