# coding=utf-8
import turtle

exit_program = False  # Boolean tests if user whats to exit the program

while not exit_program:
    option = input(('Type: [L]left [R]right [F]forward or [S]stop. Left and right turn the turtle left or\n'
                    'right however many degrees are entered, forward moves the turtle forward however far\n'
                    'you wish, and stop ends the program: '))  # gives user commands to enter to work the program

    if option == "L":
        degree = int(input("What degree left would you like to turn: "))
        turtle.left(degree)

    elif option == "R":
        degree = int(input("What degree right would you like to turn: "))
        turtle.right(degree)

    elif option == "F":
        distance = int(input("How far forward would your like to go: "))
        turtle.forward(distance)

    elif option == "S":  # if command S is typed exit program is set to True to exit while loop
        exit_program = not exit_program

    else:  # if user enters something other then the listed commands, prints invalid input
        print('\n Invalid input\n')