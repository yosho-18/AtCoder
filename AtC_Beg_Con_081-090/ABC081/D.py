n = int(input())
a = input().split()
a = [int(m) for m in a]
li = []
cnt = 0
if abs(min(a)) <= abs(max(a)):
    for i in range(1, n):
        while True:
            if a[i - 1] <= a[i]:
                break
            else:
                li.append([a.index(max(a)) + 1, i + 1])
                a[i] += max(a)
                cnt += 1

else:
    for i in range(1, n):
        while True:
            if a[-i] >= a[-i-1]:
                break
            else:
                li.append([a.index(min(a)) + 1, n - i])
                a[-i-1] += min(a)
                cnt += 1


print(cnt)
for i in range(cnt):
    print(li[i][0], li[i][1])