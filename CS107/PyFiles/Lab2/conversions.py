option = input("Would your like to convert celsius to kelvin or fahrenheit: ")

if option == "kelvin": # tests if user entered kelvin
	celsius = int(input("Please input a temperature in Celsius: ")) #Get input from user.
	celsius = float(celsius) #Make sure it is stored as a number with decimal point.
	kelvin = celsius + 273.15 #Perform conversion to Kelvin.
	print("You chose Kelvin")
	print("Kelvin temperature: " + str(kelvin)) #Display converted value.

elif option == "fahrenheit": # tests if user entered fahrenheit
	celsius = int(input("Please input a temperature in Celsius: ")) #Get input from user.
	fahrenheit = float(celsius)
	fahrenheit = celsius + 32 * 1.8
	print("You chose Fahrenheit")
	print("Fahrenheit temperature: " + str(fahrenheit))
else:
	print("INVALID INPUT") # if user enters something not equal to kelvin or fahrenheit 
	print("You entered " + option + " this is not a valid input")
