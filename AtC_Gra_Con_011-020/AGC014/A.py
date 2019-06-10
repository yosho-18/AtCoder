a, b, c = map(int, input().split())
ans = 0
if a == b and b == c:
    if a % 2 == 0:
        print(-1)
    else:
        print(0)
else:
    while True:
        if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
            tempa = b // 2 + c // 2
            tempb = c // 2 + a // 2
            tempc = a // 2 + b // 2
            a = tempa
            b = tempb
            c = tempc
            ans += 1
        else:
            break
    print(ans)