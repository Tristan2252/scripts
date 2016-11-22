import math

number = int(input("Enter a number to test if it is prime "))  # asks user to input a number
root = round(math.sqrt(number))  # takes the sqrt of the number and rounds up
count = 2  # counting number used to divide the inputed number
is_prime = True

while count <= root:
    test = number % count  # takes the remainder of number/count to see if number is divisible by anything
    if test == 0:
        print("This number is divisible by " + str(count))
        print("It is not Prime")
        is_prime = False  # if loop is executed make is_prime false
        break
    count += 1

if is_prime:  # if is_prime is still true after while loop is finished print is prime
    print("Is Prime")

