original_list = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
mapped_list = map(lambda x: x ** 2, original_list)

print(list(mapped_list))
def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "Fizz Buzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number

for ans in map(fizz_buzz, range(20)):
    print(ans)

def divide(num_1,num_2):
    try:
        print(num_1/num_2)
        print("success")
    except ZeroDivisionError:
        print('ZeroDivisionError発生')
    except:
        print('何らかの例外発生')

l = [3, 3, 2, 1, 5, 1, 4, 2, 3]
l_unique_order = sorted(set(l), key=l.index)
print(l_unique_order)
# [3, 2, 1, 5, 4]

l_2d = [[0], [2], [2], [1], [0], [0]]
def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in set(seen) and not seen.append(x)]
l_2d_unique = get_unique_list(l_2d)
print(l_2d_unique)
# [[0], [2], [1]]
l_unique = get_unique_list(l)
print(l_unique)
# [3, 2, 1, 5, 4]

l = [3, 3, 2, 1, 5, 1, 4, 2, 3]
from collections import defaultdict
d = defaultdict(int)
for i in range(len(l)):
    d[l[i]] += 1
l_duplicate = [x for x in set(l) if d[x] > 1]
print(l_duplicate)
# [1, 2, 3]