# Tìm thừa số nguyên tố của n
import math
n = int(input("Nhập n: "))
print("Thừa số nguyên tố của", n, "là", end=" ")
uocs = []
i = 2
uoc = 0
while i <= math.sqrt(n):
    if n % i == 0:
        uocs.append(i)
        uocs.append(n // i)
        uoc+=1
        n = n // i
    else:
        i += 1
print("So uoc: ", uoc)