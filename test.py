import turtle

a = input()
b = int(a)
while b!=0:
    turtle.forward(50)
    turtle.right(360/int(a))
    b = b -1
