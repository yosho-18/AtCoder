k, a, b = map(int, input().split())
if a + 1 >= b:
    print(k + 1)
else:
    if k != 1:
        t = (k - 2) % a
        w = (k - 2) // a

        i = b % a
        j = b // a

        """if t == a - 1:
            print(b * (w + 1))
        else:
            print(b * w + t)"""
        #p = ((k + 1) // (a + 2)) * (a + 2) - 1
        #print(k + 1 - p + ((k + 1) // (a + 2)) * b)
    else:
        print(2)