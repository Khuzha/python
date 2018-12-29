import math
g = 0
print(g == 0)
a = input('a = ')

while a == '0':
    print('Variable \'a\' shouldn`t be zero')
    input('a = ')
b = input('b = ')
c = input('c = ')

try:
    a = int(a)
    b = int(b)
    c = int(c)
except:
    print('Error: anyone of values isn`t correct')
    exit(1)

d = b*b - 4*a*c
print(d)

if d > 0:
    x1 = (-b - math.sqrt(d)) / (2*a)
    x2 = (-b + math.sqrt(d)) / (2*a)
    print('x1 = %.2f, x2 = %.2f' % (x2, x2))
    exit(0)
elif d == 0:
    x1 = -b / (2*a)
    print('x = %.2f' % x1)
    exit(0)
else:
    print('This equation isn`t correct. There is no root')