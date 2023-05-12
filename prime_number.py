# a = input("aの値を入力: ")
# b = input("bの値を入力: ")

# # TODO

# a = int(a)
# b = int(b)

# for i in range(2, a):
#     if a % i == 0:
#         print(f"{a}は素数ではありません")
#         break
# else:
#     print(f"{a}は素数です")

# for i in range(2, b):
#     if b % i == 0:
#         print(f"{b}は素数ではありません")
#         break
# else:
#     print(f"{b}は素数です")

def prime_num(n):
    list_n = list(n)
    if "." in list_n or "-" in list_n:
        print(f"{n}は自然数ではありません")
        return False
    else:
        n = int(n)
        for i in range(2, n):
            if n % i == 0:
                print(f"{n}は素数ではありません")
                return False
        else:
            print(f"{n}は素数です")
            return True


a = input("aの値を入力: ")

prime_num(a)
