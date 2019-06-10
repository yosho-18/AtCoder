#横にn個入力
x, y = map(int, input().split())

for k in range(100):
    s = 2**k
    t = 2**(k + 1)
    if x * s <= y and x * t > y:
        print(k + 1)
        exit()
