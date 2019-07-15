from itertools import accumulate
n, k = map(int, input().split())
a = [0] + [int(i) for i in input().split()]

accu = list(accumulate(a))

right = 0
ans = 0
for left in range(n + 1):
    while True:
        if right > n:
            print(ans)
            exit()
        tmp = accu[right] - accu[left]
        if tmp >= k:
            ans += n - right + 1
            break
        else:
            right += 1
print(ans)