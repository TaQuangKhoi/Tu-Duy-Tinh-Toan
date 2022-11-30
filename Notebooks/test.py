# Viết chương trình nhập 2 số nguyên a và b, sau đó tính và in ra giá trị phân số a/b.
# Chú ý xử lý ngoại lệ trong các tình huống dưới đây:
# Người dùng nhập a hoặc b không phải số nguyên
# Người dùng nhập b = 0


def main():
    a = input_int("Nhập a: ")
    b = input_b("Nhập b: ")
    print(a, "/", b, " = ", a / b)


def input_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x
        except ValueError:
            print("Bạn phải nhập số nguyên")


def input_b(prompt):
    x = input_int(prompt)
    if x == 0:
        print("Bạn phải nhập b khác 0")
        x = input_int("Nhập lại b: ")
        return x
    else:
        return x


main()