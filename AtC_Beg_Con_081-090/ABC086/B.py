import math
a, b = map(int, input().split())

t = 0
if 1 <= b <= 9:
    t = 10 * a + b
elif 10 <= b <= 99:
    t = 100 * a + b
else:
    t = 1000 * a + b

if math.sqrt(t) - int(math.sqrt(t)) == 0:
    print("Yes")
else:
    print("No")