a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO

a = int(a)
b = int(b)

for i in range(2, a):
    if a % i == 0:
        print(f"{a}は素数ではありません")
        break
else:
    print(f"{a}は素数です")

for i in range(2, b):
    if b % i == 0:
        print(f"{b}は素数ではありません")
        break
else:
    print(f"{b}は素数です")
