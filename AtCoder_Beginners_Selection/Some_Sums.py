n, a, b = map(int, input().split())

partsum = 0
sum = 0

for i in range(n + 1):
    j = [int(x) for x in list(str(i))]
    for k in j:
        partsum += k
    if partsum >= a and partsum <= b:
        sum += i
    partsum = 0

print(sum)