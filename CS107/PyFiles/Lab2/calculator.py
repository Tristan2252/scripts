import math

def arcsin(number):
	if number <= 1:
		if number >= -1:
			answer = math.asin(number)	
			print("The arcsos of " + str(number) + " is " + str(answer))
	else:
		print(str(number) + " is not in the domain of arcsin")

def arccos(number):
	if number <= 1:
		if number >= -1:
			answer = math.scos(number)
			print("The arccos of " + str(number) + " is " + str(answer))
	else:
		print(str(number) + " is not in the domain of arccos")

def arctan(number):
			answer = math.atan(number)
			print("The arctan of " + str(number) + " is " + str(answer))

def root(number):
	if number > 0:
			answer = math.sqrt(number)
			print("The arctan of " + str(number) + " is " + str(answer))
	else:
		print("You can't take the square root of an negative number")



number = float(input("Enter a number to use "))
operation = input("Which operation? sqrt (s), arcsin (a), arccos (c), arctan (t)")

if operation == "a":
	arcsin(number)

elif operation == "c":
	arccos(number)

elif operation == "t":
	arctan(number)

elif operation == "s":
	root(number)

else:
	print("Input not recognised")




# arcsin, arccos, arctan and square root
