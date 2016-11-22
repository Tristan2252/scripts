total = 0  # sets sum to 0 to start
exit_program = not True  # boolean to test if user wants to exit the program

while not exit_program:  # if exit_program is not true while loop stops
    number = input("Enter a number that will be added to {} :".format(total))

    if number == "exit":  # if user types exit into the input exit_program becomes true
        exit_program = True
        break

    else:
        total += int(number)  # sets number to type: int and then adds total to it
        print("Sum of numbers: {}".format(total))

print("done")