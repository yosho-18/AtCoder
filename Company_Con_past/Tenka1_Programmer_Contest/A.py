N = int(input())

for h in range(1, 3501):
    for n in range(1, 3501):
        if (4 * h * n - N * (h + n)) != 0:
            if (N * h * n) / (4 * h * n - N * (h + n)) == (N * h * n) // (4 * h * n - N * (h + n)):
                w = (N * h * n) // (4 * h * n - N * (h + n))
                if w > 0:
                    print(h, n, w)
                    exit()