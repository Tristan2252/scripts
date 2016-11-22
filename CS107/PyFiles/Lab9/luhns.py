Debug = False


def get_input():
    """
    gets user input and tests if it is valid by testing the length
    as well as if the string can be converted into an it (if it has characters)
    :return: str # string on numbers
    """
    string = input("Enter a card number: ")
    while True:
        try:
            int(string)
            if len(string) == 14:
                return string
            else:
                string = input("Invalid Number, Renter number: ")
                print("Number set to: {}".format(string))

        except ValueError:
            string = input("{} contains invalid characters\n"
                           "Enter a valid card number: ".format(string))


def mult_by2(number):
    """
    gets ever other number to the sting and converts it to an int and then
    multiples it by to and adds back to the string
    :param number: str # card number
    :return: [] # list of the each new number
    """
    num_lst = []
    for i, num in enumerate(number):
        if i % 2 == 0:
            new_num = int(num) * 2
            num_lst.append(new_num)
        else:
            num_lst.append(int(num))
    return num_lst


def sum_digits(number_lst):
    """
    takes in a list of numbers, if the number is larger then length 2 (2 digit)
    then the number is converted to a string to be split and treated as separate
    numbers to be added together and then added to overall sum.
    :param number_lst: [] # list of numbers representing the card number
    :return: int # the num of all the numbers in the list
    """
    answer = 0
    for num in number_lst:
        if num > 9:
            string_num = str(num)
            answer += int(string_num[0]) + int(string_num[1])
        else:
            answer += int(num)
    return answer


def check_card(number, card_number):
    """
    checks if the card number is valid by taking the modulus of number(sum of digits)
    if the modulus is 0 then the card is valid else the card is not
    :param number: int # sum of all the numbers in the card
    :param card_number: str # string representing the card, used for print line
    :return: str # answer presented to the user
    """
    if number % 10 == 0:
        return "\n{} is valid\n".format(card_number)
    else:
        return "\n{} is NOT valid\n".format(card_number)


def luhns():
    if Debug:
        input_num = "38520000023237"
    else:
        input_num = get_input()

    num_lst = mult_by2(input_num)
    num_sum = sum_digits(num_lst)
    print(check_card(num_sum, input_num))


if __name__ == '__main__':
    luhns()