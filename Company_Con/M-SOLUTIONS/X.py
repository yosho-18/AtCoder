n, k = map(int, input().split())
s = input()
if n == 1:
    print(1)
if n != 1:
    nums = []
    cnt = 1
    for i in range(1, n):
        if s[i - 1] != s[i]:
            nums.append([s[i - 1], cnt])
            cnt = 1
            if i == n - 1:
                nums.append([s[i], cnt])
        else:
            cnt += 1
            if i == n - 1:
                nums.append([s[i - 1], cnt])

    candi = 0
    ansli = []
    p = 0
    for i in range(len(nums)):
        if nums[i][0] == "0":
            p += 1
    k = min(k, p)

    i1 = 0
    j1 = 0
    while i1 <= k and j1 < len(nums):
        if i1 == k and nums[j1][0] == "0":
            pass
        else:
            candi += nums[j1][1]
        if nums[j1][0] == "0":
            i1 += 1
        j1 += 1
    ansli.append(candi)
    if candi == n:
        print(n)
        exit()

    a = 0
    b = j1 - 1
    while b < len(nums):
        for i in range(2):
            if nums[a + i][0] == "1":
                candi -= nums[a + i][1]
            elif nums[a + i][0] == "0":
                candi -= nums[a + i][1]
                a += i + 1
                break
        for i in range(2):
            if b + i >= len(nums):
                ansli.append(candi)
                b += 1
                break
            else:
                if nums[b + i][0] == "1":
                    candi += nums[b + i][1]
                    b += i + 1
                    ansli.append(candi)
                    break
                elif nums[b + i][0] == "0":
                    candi += nums[b + i][1]

    print(max(ansli))