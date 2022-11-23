# Cho ds M = [[1], [1, 2, 4, 6, 8], [1, 2, 10], [1, 2, 3, 4]]. Hãy in ra list dài nhất trong danh sách này.
M = [[1], [1, 2, 4, 6, 8], [1, 2, 10], [1, 2, 3, 4]]
max = len(M[0])
index = 0
for i in range(1, len(M)):
    if len(M[i]) > max:
        max = len(M[i])
        index = i

print("List dài nhất trong danh sách M: ", M[index])
print("Độ dài:", max)