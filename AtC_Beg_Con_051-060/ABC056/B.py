W, a, b = map(int, input().split())
if b + W < a:
    print(a - b - W)
elif a + W >= b + W >= a or a <= b <= a + W:
    print(0)
elif b > a + W:
    print(b - a - W)