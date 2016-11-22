# coding=utf-8
import turtle

'function takes in a list of directions and iterates through each tuple in the list'
'if the string of index 0 is equal to one of the strings in the if statements then the'
'designated action for turtle is preformed with the value of index 1 in the tuple'
def direct(directions):
    for i in directions:
        if i[0] == "F":
            turtle.forward(i[1])
        elif i[0] == "L":
            turtle.left(i[1])
        elif i[0] == "R":
            turtle.right(i[1])


def main():
    exit_program = False  # Boolean tests if user whats to exit the program
    directions = []
    while not exit_program:
        option = input(('Type: [L]left [R]right [F]forward or [S]stop. Left and right turn the turtle left or\n'
                        'right however many degrees are entered, forward moves the turtle forward however far\n'
                        'you wish, and stop ends the program: '))  # gives user commands to enter to work the program

        if option == "L":
            degree = int(input("What degree left would you like to turn: "))
            directions.append(("L", degree))

        elif option == "R":
            degree = int(input("What degree right would you like to turn: "))
            directions.append(("R", degree))

        elif option == "F":
            distance = int(input("How far forward would your like to go: "))
            directions.append(("F", distance))

        elif option == "S":  # if command S is typed exit program is set to True to exit while loop
            exit_program = not exit_program

        else:  # if user enters something other then the listed commands, prints invalid input
            print('\n Invalid input\n')

    print("\n {} \n".format(directions))
    direct(directions)


if __name__ == '__main__':
    main()