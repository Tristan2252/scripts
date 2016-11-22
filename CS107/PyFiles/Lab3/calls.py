

def charge_card(charge):  # charge card function, input the amount to add to account and final charge is determined
    # charge_value = 1   (test variable)
    if (charge <= 25) and (charge >= 10):  # if else statements test the value and add the necessary amount
        final_value = charge + 3
        print("{} dollars was added to your account".format(final_value))
    elif (charge <= 50) and (charge > 25):
        final_value = charge + 8
        print("{} dollars was added to your account".format(final_value))
    elif (charge <= 100) and (charge > 50):
        final_value = charge + 20
        print("{} dollars was added to your account".format(final_value))
    elif charge > 100:
        final_value = charge + 25
        print("{} dollars was added to your account".format(final_value))
    elif charge < 10:
        final_value = charge
        print("{} dollars was added to your account".format(final_value))
    else:
        print("INVALID INPUT")


def main():  # main function , asks user for charge value and calls function
    charge_value = int(input("Enter the value you want to charge: "))
    charge_card(charge_value)

if __name__ == "__main__":
    main()
