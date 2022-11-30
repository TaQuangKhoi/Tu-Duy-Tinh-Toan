# 2. Viết chương trình yêu cầu người dùng nhập a, b và c là độ dài 3 cạnh của một tam giác.
# Xử lý ngoại lệ trong các tình huống sau:
# Người dùng nhập a, b hoặc c không phải là kiểu số
# Người dùng nhập giá trị 0 hoặc số âm cho a, b hoặc c
# Người dùng nhập a, b, c dương nhưng không thể là cạnh của một tam giác

class ValueNotZeroError(Exception):
    """Not zero value"""
    pass


class ValueSmallThanZeroError(Exception):
    """Value small than zero"""
    pass


class NotTriangleError(Exception):
    """Not triangle"""
    pass


def main():
    while True:
        try:
            a = input_int("Nhập a: ")
            b = input_int("Nhập b: ")
            c = input_int("Nhập c: ")
            if check_triangle(a, b, c):
                raise NotTriangleError
            else:
                print("Đây là 3 cạnh của tam giác")
                break
        except NotTriangleError:
            print("Không phải là tam giác")


def input_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            if x == 0:
                raise ValueNotZeroError
            if x < 0:
                raise ValueSmallThanZeroError
            return x
        except ValueError:
            print("Bạn phải nhập số nguyên")
        except ValueNotZeroError:
            print("Bạn phải nhập số khác 0")
        except ValueSmallThanZeroError:
            print("Bạn phải nhập số dương")


def check_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return True


main()
