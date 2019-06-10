a, b, t = map(int, input().split())
t = t+0.5
for i in range(100):
    if i * a <= t <= (i + 1) * a:
        print(i * b)
        exit()