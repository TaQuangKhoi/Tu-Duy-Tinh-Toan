

# def isfloat(num):
#     try:
#         float(num) # Check bằng ép kiểu
#         return True
#     except ValueError:
#         return False

# canh_a = input("Nhập cạnh a: ")
# while(isfloat(canh_a) == False):
#     canh_a = input("Nhập lại cạnh a: ")

# canh_b = input("Nhập cạnh b: ")
# while(isfloat(canh_b) == False):
#     canh_b = input("Nhập lại cạnh a: ")

# canh_c = input("Nhập cạnh c: ")
# while(isfloat(canh_c) == False):
#     canh_c = input("Nhập lại cạnh a: ")

# def isTamGiac (a,b,c):
#     return a+b>c and a+c>b and b+c>a



import turtle
import math

pen = turtle.Pen()

mau = ['red', 'blue', 'green']

def veTamGiac(_a, _b, _c):
    pen.color(mau[0])
    pen.fd(_a)
    pen.left(90)
    cosa = (_a**2+_c**2-_b**2)/2*_a*_b
    print(cosa)
    print(math.cos(math.pi/cosa))


veTamGiac(2, 3, 4)

# if(isTamGiac(canh_a,canh_b,canh_c)):
#     print("Bắt đầu vẽ tam giác")
#     veTamGiac(20, 30, 40)