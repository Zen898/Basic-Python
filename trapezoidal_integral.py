from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
from math import pi
from math import exp
from math import sqrt

# a = 0
# b = pi/2
# n = 100

# h = (b - a)/n
# s = 0
# for i in range(1, n + 1):
#     s += sin((i-1)*h) + sin(i*h)
# sum = (h/2)*s
# print(sum)


def s(x):
    return sin(x)


def g(x):
    return 4/(1 + x**2)


def z(x):
    return sqrt(pi)*exp(-((x)**2))


def trape_int(f, a=0, b=1, n=100):
    h = (b - a)/n
    s = 0
    for i in range(1, n + 1):
        s += f(a + (i-1)*h) + f(a + i*h)
    sum = (h/2)*s
    print(sum)
    return sum


trape_int(z, -100, 100, 1000)
