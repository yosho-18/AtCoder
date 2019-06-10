#横にn個入力
a, b = map(int, input().split())
count = 0
for i in range(1,a + 1):
    if i < a:
        for j in range(1,31):
            if i == j:
                count += 1
    if i == a:
        for j in range(1,b + 1):
            if i == j:
                count += 1

print(count)

