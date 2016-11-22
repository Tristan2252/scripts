import turtle

number = int(input("Enter the amount of sides: "))
count = 0
angle = 180 * (number - 2)/number  # finds the degree of every angle in the polygon

while count < number:
        turtle.forward(100)  # draws 100 forward
        turtle.left(180 - angle)  # tells turtle to turn left 180 - angle degrees
        count += 1

input("Type any key to exit: ")  # leaves turtle open till user types something