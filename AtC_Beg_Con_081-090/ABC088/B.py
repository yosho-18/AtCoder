n = int(input())
a = input().split()
a = [int(m) for m in a]

a.sort(reverse=True)

ali = []
bli = []

for i in range(n):
    if i % 2 == 0:
        ali.append(a[i])
    else:
        bli.append(a[i])
print(sum(ali) - sum(bli))