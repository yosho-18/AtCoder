n = int(input())
a = list(map(int, input().split()))
cli = {}
for i in range(-1,10**5+1):
  cli[i] = 0
for j in a:
  cli[j - 1] += 1
  cli[j] += 1
  cli[j + 1] += 1
print(max(cli.values()))
