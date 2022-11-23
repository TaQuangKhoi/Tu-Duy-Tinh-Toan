import os

os.chdir('C:\\My_Repos\\GitHub\\TaQuangKhoi\\Tu-Duy-Tinh-Toan-1')
path = "text.txt"

x = []

f = open(path , "r")
n = int(f.readline())
line = f.readline()
line = line.split()

for i in line:
    x.append(float(i))

f.close()

print("Tổng ptử", n)
print("Mảng là: ", x)

# max of x
max = x[0]
for i in range(1, len(x)):
    if max < x[i]:
        max = x[i]

print("Max value in x: ", max)

# total of x
total = 0
for i in range(len(x)):
    total += x[i]

print("Total of x: ", total)