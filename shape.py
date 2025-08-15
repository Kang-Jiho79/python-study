import turtle

while True:
    shape = input("circle / triangle / rectangle / quit \n")
    turtle.reset()
    if shape == "quit":
        break
    elif shape == "circle":
        turtle.circle(50)
    elif shape == "triangle":
        for i in range(3):
            turtle.forward(100)
            turtle.left(120)
    elif shape == "rectangle":
        for i in range(4):
            turtle.forward(100)
            turtle.left(90)
    else:
        print("잘못입력하였습니다")
turtle.bye()
