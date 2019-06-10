import sys
N = int(input())
for i in range(1, N):
    print("? {} {}".format(i, N))
    sys.stdout.flush()
    dist = int(input())
