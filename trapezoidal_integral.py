from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------

from math import pi
a = 0
b = pi/2
n = 100

h = (b - a)/n
s = 0
for i in range(1, n + 1):
    s += sin((i-1)*h) + sin(i*h)
sum = (h/2)*s
print(sum)
