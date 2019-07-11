n = int(input())
cnt = 0
for i in range(1, 6 * 10 ** 5):
    if len(set(str(i))) == 1:
        cnt += 1
    if cnt == n:
        print(i)
        break