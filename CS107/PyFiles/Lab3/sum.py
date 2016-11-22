

def recurse(number):

    if number == 1:
        return 1
    else:
        return number + recurse(number-1)


def main():
    number = int(input("Enter a number to be summed up to: "))
    # recurse(10)
    recurse(number)
    print("The sum of the numbers between 1 and {} is: {}".format(number, recurse(number)))

if __name__ == "__main__":
    main()