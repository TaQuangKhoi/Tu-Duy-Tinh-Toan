dic = {}
sohs = int(input("Nhập số hs:"))
for i in range(sohs):
    name = input("Nhập tên: ")
    while name in dic:
        print("Tên đã tồn tại")
        name = input("Nhập tên khác: ")
    
    diem = input("Nhập điểm: ")
    while diem.isdigit() == False:
        print("Điểm không phù hợp")
        diem =input("Nhập điểm: ")
    
    dic[name] = float(diem)

dic