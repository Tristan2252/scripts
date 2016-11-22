def palindrome(string, test=None):
    """
    tests if string is palindrome by testing firs an last letters
    in the string and then subtracting them from the string to pass
    it through the function again/
    :param string: str # word to test
    :param test: Boolean # if it is or is not True
    :return: Boolean # ' '  ' '
    """
    if len(string) == 0:
        return test
    if string[0] == string[-1]:
        new_string = string[1:-1]
        return palindrome(new_string, True)
    else:
        return False


def main():
    word = input("Enter potential palindrome: ")
    print(palindrome(word))


if __name__ == '__main__':
    main()