import math
x1, y1, x2, y2 = map(int, input().split())
p3 = 0
q3 = 0
p4 = 0
q4 = 0

for x3 in range(-301, 301):
    for y3 in range(-301, 301):
        length1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        length2 = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
        if x2 != x1 and x3 != x2:
            slope = (y2 - y1)/(x2 - x1)*(y3 - y2)/(x3 - x2)
            if y1 != y2 and length1 == length2 and slope == -1 and\
                x2 > x1 and y3 > (y2 - y1)/(x2 - x1)*x3 +(x2*y1 - y2*x1)/(x2 - x1):
                p3 = x3
                q3 = y3
            elif y1 != y2 and length1 == length2 and slope == -1 and\
                x2 < x1 and y3 < (y2 - y1)/(x2 - x1)*x3 +(x2*y1 - y2*x1)/(x2 - x1):
                p3 = x3
                q3 = y3
        else:
            if x2 == x1 and y2 > y1 and y3 == y2 and x3 == x2 - length1:
                p3 = x3
                q3 = y3
            elif x2 == x1 and y2 < y1 and y3 == y2 and x3 == x2 + length1:
                p3 = x3
                q3 = y3
            elif x2 > x1 and y2 == y1 and x3 == x2 and y3 == y2 + length1:
                p3 = x3
                q3 = y3
            elif x2 < x1 and y2 == y1 and x3 == x2 and y3 == y2 - length1:
                p3 = x3
                q3 = y3

for x4 in range(-301, 301):
    for y4 in range(-301, 301):
        length1 = math.sqrt((p3 - x2)**2 + (q3 - y2)**2)
        length2 = math.sqrt((x4 - p3)**2 + (y4 - q3)**2)
        if x2 != p3 and p3 != x4:
            slope = (q3 - y2)/(p3 - x2)*(y4 - q3)/(x4 - p3)
            if y2 != q3 and length1 == length2 and slope == -1 and\
                p3 > x2 and y4 > (q3 - y2)/(p3 - x2)*x4 +(p3*y2 - q3*x2)/(p3 - x2):
                p4 = x4
                q4 = y4
            elif y2 != q3 and length1 == length2 and slope == -1 and\
                p3 < x2 and y4 < (q3 - y2)/(p3 - x2)*x4 +(p3*y2 - q3*x2)/(p3 - x2):
                p4 = x4
                q4 = y4
        else:
            if p3 == x2 and q3 > y2 and y4 == q3 and x4 == p3 - length1:
                p4 = x4
                q4 = y4
            elif p3 == x2 and q3 < y2 and y4 == q3 and x4 == p3 + length1:
                p4 = x4
                q4 = y4
            elif p3 > x2 and q3 == y2 and x4 == p3 and y4 == q3 + length1:
                p4 = x4
                q4 = y4
            elif p3 < x2 and q3 == y2 and x4 == p3 and y4 == q3 - length1:
                p4 = x4
                q4 = y4

print(p3, q3, p4, q4)
