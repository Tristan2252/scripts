 
# FIZZ BUZZ: asks user to input a positive number and then assignes in to "number"

number = int(input("Please input a positive integer "))

# tests if the number is positive by checking if it is grater then 0
if number > 0:
    count = 0 # variable used to count from 0 to inputed number
    while count < number:
        # adds 1 to count everytiem the while loop is executed
        count = count + 1

        # takes the remander of count / 3 and count / 5
        fizz = count%3
        buzz = count%5

        # checks for numbers divisable by 3 AND 5
        if ((fizz == 0) and (buzz == 0)):
            print("{}".format(count) + " Fizz Buzz")
        elif fizz == 0:
            print("{}".format(count) + " Fizz")
        elif buzz == 0:
            print("{}".format(count) + " Buzz")
        # if none of the conditions are met just prints count
        else:
            print(str(count))

# if the number is lesss the 0 invalid message is printed
else:
    print("Invalid input, must be a positive number")

