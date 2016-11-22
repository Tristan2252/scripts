# caracter = input("Enter R, P, or S >>> ")

check_input = False
while check_input == False:
        caracter = input("Enter R, P, or S >>> ")

        if caracter == "R":
            print("You chose rock. Exiting...")
            check_input = True
        elif caracter == "P":
            print("You chose paper. Exiting...")
            check_input = True
        elif caracter == "S":
            print("You chose scissors. Exiting...")
            check_input = True
        else:
            print("Did not enter R, P, or S. Try again.")
            check_input = False