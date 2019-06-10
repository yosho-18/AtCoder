a, b, k = map(int, input().split())
cnt = 0
li = []
for i in range(1, 101):
    if a % i == 0 and b % i == 0:
        cnt += 1
        li.append(i)

li.sort(reverse = True)
print(li[k - 1])