n,k=map(int, input().split())
s = input()
nums = []
sums = []
cnt = 1
for i in range(1, n):
    if s[i - 1] != s[i]:
        nums.append(int(s[i - 1]))
        sums.append(cnt)
        cnt = 1
    else:
        cnt += 1

candi = 0
ansli = []
if s[0] == "0":
    if s[-1] == "0":
        k = min(k, len(sums)//2 + 1)
        candi = sum(sums[:2 * k])
        ansli.append(candi)
        for i in range(1, len(sums)//2 + 2):
            if i == 1:
                candi = candi - sums[0] + sums[2 * k] + sums[2 * k + 1]
            else:
                pass
else:
    pass