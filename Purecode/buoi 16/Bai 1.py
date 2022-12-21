def checkInt(so_nguyen):
    if so_nguyen.isdigit():
        return True
    else: 
        return False

so_nguyen_1 = input("Nhập số nguyên 1: ")
while(checkInt(so_nguyen_1) == False):
    so_nguyen_1 = input("Nhập lại số nguyên 1: ")


so_nguyen_2 = input("Nhập số nguyên 2: ")
while(checkInt(so_nguyen_2) == False):
    so_nguyen_2 = input("Nhập lại số nguyên 2: ")


tong = int(so_nguyen_1) + int(so_nguyen_2)
print ("Tổng là", tong)