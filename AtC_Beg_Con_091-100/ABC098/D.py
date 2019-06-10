n = int(input())
a = input().split()
a = [int(m) for m in a]
k = 1
i = 0
t = a[0]
count = 1
p = 0
if n != 1:
    while i < n:
        if i != 0:
            t -= a[i - 1]
            if p == 1:
                count += k - i + 1
            else:
                count += k - i
        if p != 1:
            for j in range(k, n):
                if t + a[j] == t ^ a[j]:
                    t += a[j]
                    count += 1
                    if j == n - 1:
                        k = j
                        p = 1
                        i += 1
                else:
                    k = j
                    i += 1
                    break
        else:
            i += 1
    print(count)
else:
    print(count)
