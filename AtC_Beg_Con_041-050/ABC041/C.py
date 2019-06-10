n = int(input())
a = input().split()
a = [[m + 1, int(a[m])] for m in range(len(a))]
a.sort(key=lambda x:(x[1]), reverse=True)
for i in range(n):
    print(a[i][0])
