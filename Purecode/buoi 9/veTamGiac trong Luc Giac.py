from turtle import *
rua = Turtle()

# Array with six colors
colors = ['red', 'yellow', 'green', 'blue', 'purple', 'brown']

def tamgiac(color):
    rua.fillcolor(color)
    rua.begin_fill()
    for y in range(3):
        rua.forward(100)
        rua.left(120)
    rua.right(60)
    rua.end_fill()

for i in range(6):
    tamgiac(colors[i])