import math

# functions that find circumference, diameter, area to be used in the program
def circumference(radius):
	circumference = 2 * math.pi * radius
	return circumference  # returns answer

def diameter(radius):
	diameter = radius * 2
	return diameter

def area(radius):
	area = math.pi * radius**2 
	return area

# object used to test what the user is asking for, if user inputs the name of the 
# function they want to preform it will be tested by if / else statements that decide
# witch function to execute.

option = input("Type what you would like to find: circumference, diameter, or area of a circle ")

# asks the user to input the radius of the circle to be used
radius = int(input("What is the radius of the circle? "))

if option == "circumference": # if the string is equal to the specifies string it will be executed
	answer = circumference(radius)
	print("The Circumference is: " + str(answer)) #prints answer as a string

elif option == "diameter":
	answer = diameter(radius)
	print("The Diameter is: " + str(answer))

elif option == "area":
	answer = area(radius)
	print("Answer: " + str(answer))

# if user input is incorrect else is executed
else:
	print("PROGRAM FAIL, incorrect input") 
