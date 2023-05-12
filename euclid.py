a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO

# if b > a:
#     (a, b) = (b, a)

# a = int(a)
# b = int(b)

# while b != 0:
#     (a, b) = (b, a % b)

# print(a)

# 問3


def euclid(a, b):
    if b > a:
        (a, b) = (b, a)

    a = int(a)
    b = int(b)

    while b != 0:
        (a, b) = (b, a % b)

    print(f"最大公約数は{a}")
    return a


# euclid(a, b)


# 問4


def prime_euclid(a, b):
    if euclid(a, b) == 1:
        print(f"従って{a}と{b}は互いに素です")
    else:
        print(f"従って{a}と{b}は互いに素ではありません")


prime_euclid(a, b)
