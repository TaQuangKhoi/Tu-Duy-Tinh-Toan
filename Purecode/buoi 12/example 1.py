import os

os.chdir('C:\\My_Repos\\GitHub\\TaQuangKhoi\\Tu-Duy-Tinh-Toan')

path = "text.txt"

x = []

f = open(path, "r")
lines = f.readlines()
print(len(lines))


def first():
    print("===In ra 5 dòng đầu===")
    for i in range(5):
        print(lines[i])


def second():
    print("In ra 5 dòng cuối")
    for y in range(-5, 0):
        print(lines[y])


if len(lines) < 5:
    print("===Nhỏ hơn 5===")
    for r in range(len(lines)):
        print(lines[r])
else:
    first()
    second()

