#横にn個入力
x, a, b = map(int, input().split())
if a - b >= 0:
    print("delicious")
elif x + a - b >= 0:
    print("safe")
else:
    print("dangerous")