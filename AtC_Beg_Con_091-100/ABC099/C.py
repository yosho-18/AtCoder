
n = int(input())

ark = float("INF")
if n < 50000:
    for l in range(2):  # 59049
        abc = (n - (59049*l))
        if abc < 0:
            break
        for k in range(3):  # 46656
            abc = (n - (46656 * k+59049*l))
            if abc < 0:
                break
            for j in range(6):  # 7776
                abc = (n - (776 * j + 46656 * k+59049*l))
                if abc < 0:
                    break
                for h in range(4):  # 1296,6
                    abc = (n - (1296 * h+ 7776 * j + 46656 * k+59049*l))
                    if abc < 0:
                        break
                    for g in range(6):  # 729,9
                        abc = (n - (729 * g + 1296 * h+ 7776 * j + 46656 * k+59049*l))
                        if abc < 0:
                            break
                        for f in range(4):#216,5(4)
                            abc = (n - (216 * f+ 729 * g + 1296 * h+ 7776 * j + 46656 * k+59049*l))
                            if abc < 0:
                                break
                            for e in range(4):  # 81
                                abc = (n - (81 * e + 216 * f + 729 * g + 1296 * h+ 7776 * j + 46656 * k+59049*l))
                                if abc < 0:
                                    break
                                for d in range(5):  # 36
                                    abc = (n - (36 * d + 81 * e + 216 * f + 729 * g + 1296 * h+ 7776 * j + 46656 * k+59049*l))
                                    if abc < 0:
                                        break
                                    for c in range(4):  # 9
                                        abc = (n - (9 * c + 36 * d + 81 * e + 216 * f + 729 * g + 1296 * h + 7776 * j + 46656 * k+59049*l))
                                        if abc < 0:
                                            break
                                        for b in range(3):  # 6
                                            abc = (n - (6 * b + 9 * c + 36 * d + 81 * e + 216 * f + 729 * g + 1296 * h + 7776 * j + 46656 * k+59049*l))
                                            if abc < 0:
                                                break
                                            for a in range(6):  # 1
                                                abc = (n - (1*a+6*b+9*c+36*d+81*e+216*f+729*g+1296*h+7776*j+46656*k+59049*l))
                                                if abc < 0:
                                                    break
                                                if abc % 6561 == 0 and abc >= 0:
                                                    i = abc//6561
                                                    if ark > a+b+c+d+e+f+g+h+i+j+k+l:
                                                        ark = a+b+c+d+e+f+g+h+i+j+k+l
else:
    for l in range(2):  # 59049
        abc = (n - (59049*l))
        if abc < 0:
            break
        for k in range(3):  # 46656
            abc = (n - (46656 * k+59049*l))
            if abc < 0:
                break
            for j in range(6):  # 7776
                abc = (n - (776 * j + 46656 * k+59049*l))
                if abc < 0:
                    break
                for h in range(3):  # 1296,6
                    abc = (n - (1296 * h+ 7776 * j + 46656 * k+59049*l))
                    if abc < 0:
                        break
                    for g in range(4):  # 729,9
                        abc = (n - (729 * g + 1296 * h+ 7776 * j + 46656 * k+59049*l))
                        if abc < 0:
                            break
                        for f in range(3):#216,5(4)
                            abc = (n - (216 * f+ 729 * g + 1296 * h+ 7776 * j + 46656 * k+59049*l))
                            if abc < 0:
                                break
                            for e in range(4):  # 81
                                abc = (n - (81 * e + 216 * f + 729 * g + 1296 * h+ 7776 * j + 46656 * k+59049*l))
                                if abc < 0:
                                    break
                                for d in range(5):  # 36
                                    abc = (n - (36 * d + 81 * e + 216 * f + 729 * g + 1296 * h+ 7776 * j + 46656 * k+59049*l))
                                    if abc < 0:
                                        break
                                    for c in range(4):  # 9
                                        abc = (n - (9 * c + 36 * d + 81 * e + 216 * f + 729 * g + 1296 * h + 7776 * j + 46656 * k+59049*l))
                                        if abc < 0:
                                            break
                                        for b in range(3):  # 6
                                            abc = (n - (6 * b + 9 * c + 36 * d + 81 * e + 216 * f + 729 * g + 1296 * h + 7776 * j + 46656 * k+59049*l))
                                            if abc < 0:
                                                break
                                            for a in range(6):  # 1
                                                abc = (n - (1*a+6*b+9*c+36*d+81*e+216*f+729*g+1296*h+7776*j+46656*k+59049*l))
                                                if abc < 0:
                                                    break
                                                if abc % 6561 == 0 and abc >= 0:
                                                    i = abc//6561
                                                    if ark > a+b+c+d+e+f+g+h+i+j+k+l:
                                                        ark = a+b+c+d+e+f+g+h+i+j+k+l
print(ark)
"""n = int(input())

ar = []
for a in range(6):#1
    abc = (n - (1 * a))
    if abc < 0:
        break
    for b in range(3):#6
        abc = (n - (1 * a + 6 * b))
        if abc < 0:
            break
        for c in range(4):#9
            abc = (n - (1 * a + 6 * b + 9 * c))
            if abc < 0:
                break
            for d in range(5):#36
                abc = (n - (1 * a + 6 * b + 9 * c + 36 * d))
                if abc < 0:
                    break
                for e in range(4):#81
                    abc = (n - (1 * a + 6 * b + 9 * c + 36 * d + 81 * e))
                    if abc < 0:
                        break
                    for f in range(5):#216
                        abc = (n - (1 * a + 6 * b + 9 * c + 36 * d + 81 * e + 216 * f))
                        if abc < 0:
                            break
                        for g in range(9):#729
                            abc = (n - (1 * a + 6 * b + 9 * c + 36 * d + 81 * e + 216 * f + 729 * g))
                            if abc < 0:
                                break
                            for h in range(6):#1296
                                abc = (n - (1 * a + 6 * b + 9 * c + 36 * d + 81 * e + 216 * f + 729 * g + 1296 * h))
                                if abc < 0:
                                    break
                                for j in range(6):#7776
                                    abc = (n - (1 * a + 6 * b + 9 * c + 36 * d + 81 * e + 216 * f + 729 * g + 1296 * h + 7776 * j))
                                    if abc < 0:
                                        break
                                    for k in range(3):#46656
                                        abc = (n - (1 * a + 6 * b + 9 * c + 36 * d + 81 * e + 216 * f + 729 * g + 1296 * h + 7776 * j + 46656 * k))
                                        if abc < 0:
                                            break
                                        for l in range(2):#59049
                                            abc = (n - (1*a+6*b+9*c+36*d+81*e+216*f+729*g+1296*h+7776*j+46656*k+59049*l))
                                            if abc < 0:
                                                break
                                            if abc % 6561 == 0 and abc >= 0:
                                                i = abc//6561
                                                ar.append(a+b+c+d+e+f+g+h+i+j+k+l)
print(min(ar))"""
"""ar = []
for a in range(6):#1
    for b in range(3):#6
        for c in range(4):#9
            for d in range(5):#36
                for e in range(4):#81
                    for f in range(5):#216
                        for g in range(9):#729
                            for h in range(6):#1296
                                for i in range(9):#6561
                                    for j in range(6):#7776
                                        for k in range(3):#46656
                                            for l in range(2):#59049
                                                if 1*a+6*b+9*c+36*d+81*e+216*f+729*g+1296*h+6561*i+7776*j+46656*k+59049*l == n:
                                                    ar.append(a+b+c+d+e+f+g+h+i+j+k+l)
print(min(ar))"""