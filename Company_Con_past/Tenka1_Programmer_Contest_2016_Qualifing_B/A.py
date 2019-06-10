ans = 20

def f(n):
    return (n ** 2 + 4) // 8
for i in range(3):
    ans = f(ans)
print(ans)