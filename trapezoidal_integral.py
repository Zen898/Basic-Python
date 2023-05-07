from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------

from math import pi

h = (pi/2)/100
s = 0
for i in range(1, 101):
    s += sin((i-1)*h) + sin(i*h)
sum = (h/2)*s
print(sum)
