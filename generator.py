# Câu 1
import turtle

mausac = ["red", "green", "blue", "orange", "pink", "yellow"]

# Lục giác
lg = turtle.Pen()

for i in 6:
    lg.forward(50)


# Order form small to large
# unsorted Array with 11 elements
A = [12, 11, 13, 5, 6, 7, 8, 9, 10, 1, 2]
print("First array: ", A)

for i in range(len(A) - 1):
    for j in range(i+1, len(A)):
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]

print("Array after sort: ", A)

# Create a matrix
# m x n
matrix = []
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

for i in range(m):
    print("Enter row ", i+1, ";")
    row = []
    for j in range(n):
        x = int(input("Enter element  ", str(j+1), "th: "))
        row.append(x)
    matrix.append(row)

print("Matrix: ", matrix)

# print matrix with beatufull format
for i in range(m):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()