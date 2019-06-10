n = int(input())
d = len(str(n)) - 1
k = str(n)
j = int(k[0])
count = 1
co = 0
for i9 in range(3, 8, 2):
    for i8 in range(3, 8, 2):
        for i7 in range(3, 8, 2):
            for i6 in range(3, 8, 2):
                for i5 in range(3, 8, 2):
                    for i4 in range(3, 8, 2):
                        for i3 in range(3, 8, 2):
                            for i2 in range(3, 8, 2):
                                for i1 in range(3, 8, 2):
                                    if len(set([i9,i8,i7,i6,i5,i4,i3,i2,i1])) == 3:
                                        t = int(str(i9) + str(i8) + str(i7) + str(i6) + str(i5) + str(i4) + str(i3) + str(i2) + str(i1))
                                        if t <= n:
                                            co += 1
for i8 in range(3, 8, 2):
    for i7 in range(3, 8, 2):
        for i6 in range(3, 8, 2):
            for i5 in range(3, 8, 2):
                for i4 in range(3, 8, 2):
                    for i3 in range(3, 8, 2):
                        for i2 in range(3, 8, 2):
                            for i1 in range(3, 8, 2):
                                if len(set([i8,i7, i6, i5, i4, i3, i2, i1])) == 3:
                                    t = int(str(i8) + str(i7) + str(i6) + str(i5) + str(i4) + str(i3) + str(i2) + str(i1))
                                    if t <= n:
                                        co += 1
for i7 in range(3, 8, 2):
    for i6 in range(3, 8, 2):
        for i5 in range(3, 8, 2):
            for i4 in range(3, 8, 2):
                for i3 in range(3, 8, 2):
                    for i2 in range(3, 8, 2):
                        for i1 in range(3, 8, 2):
                            if len(set([i7, i6, i5, i4, i3, i2, i1])) == 3:
                                t = int(str(i7) + str(i6) + str(i5) + str(i4) + str(i3) + str(i2) + str(i1))
                                if t <= n:
                                    co += 1

for i6 in range(3, 8, 2):
    for i5 in range(3, 8, 2):
        for i4 in range(3, 8, 2):
            for i3 in range(3, 8, 2):
                for i2 in range(3, 8, 2):
                    for i1 in range(3, 8, 2):
                        if len(set([i6, i5, i4, i3, i2, i1])) == 3:
                            t = int(str(i6) + str(i5) + str(i4) + str(i3) + str(i2) + str(i1))
                            if t <= n:
                                co += 1
for i5 in range(3, 8, 2):
    for i4 in range(3, 8, 2):
        for i3 in range(3, 8, 2):
            for i2 in range(3, 8, 2):
                for i1 in range(3, 8, 2):
                    if len(set([i5, i4, i3, i2, i1])) == 3:
                        t = int(str(i5) + str(i4) + str(i3) + str(i2) + str(i1))
                        if t <= n:
                            co += 1
for i4 in range(3, 8, 2):
    for i3 in range(3, 8, 2):
        for i2 in range(3, 8, 2):
            for i1 in range(3, 8, 2):
                if len(set([i4, i3, i2, i1])) == 3:
                    t = int(str(i4) + str(i3) + str(i2) + str(i1))
                    if t <= n:
                        co += 1
for i3 in range(3, 8, 2):
    for i2 in range(3, 8, 2):
        for i1 in range(3, 8, 2):
            if len(set([i3, i2, i1])) == 3:
                t = int(str(i3) + str(i2) + str(i1))
                if t <= n:
                    co += 1

print(co)
"""for i in range(3, d):
    co += 3 ** i - 3 * 2 ** i + 3
if 0 < j < 3:
    co += 3 ** d - 3 * 2 ** d + 3
elif 3 <= j < 5:
    for u
elif 5 <= j < 7:
    count *= 2
elif 7 <= j:
    count *= 3"""
"""li = [6, ]
for i in range(d, 0, -1):
    if i >= 3:
        count *= 3
    elif i == 2 and d + 1 > 2:
        count *= 2
    elif d + 1 <= 2:
        count = 0
if 5 <= j < 7:
    count *= 2
elif 7 <= j:
    count *= 3
print(count)"""
