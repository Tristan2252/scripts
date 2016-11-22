def ends(string):
    return "{}{}{}{}".format(string[0], string[1], string[-2], string[-1])  # prints the strings of the indexes


def mix(string1, string2):
    end_letters1 = string1[1:]  # makes a list of the end letters
    end_letters2 = string2[1:]
    first_letter1 = string1[0]  # makes a list of the firs letter
    first_letter2 = string2[0]
    return "{}{} {}{}".format(first_letter2, end_letters1, first_letter1, end_letters2)


def split(string1, string2):
    length_str1 = len(string1)  # gets the length of the string imputed
    length_str2 = len(string2)
    half1 = length_str1 // 2  # splits the length of the imputed string in half
    half2 = length_str2 // 2
    if (length_str1 % 2 == 0) and (length_str2 % 2 == 0):  # tests if both strings are even
        return "{}{}{}{}".format(string1[:half1], string2[:half2], string1[half1:], string2[half2:])
        # above, prints half the the strings inputted alternating front A front B back A....

    elif length_str1 % 2 == 0 and length_str2 % 2 != 0:  # test the length of string 2 to be even
        return "{}{}{}{}".format(string1[:half1], string2[:half2+1], string1[half1:], string2[half2+1:])

    elif length_str1 % 2 != 0 and length_str2 % 2 == 0:  # test the length of string 2 to be even
        return "{}{}{}{}".format(string1[:half1+1], string2[:half2], string1[half1+1:], string2[half2:])

    elif length_str1 % 2 != 0 and length_str2 % 2 != 0:  # test the length of string 1 and 2 to be !even
        return "{}{}{}{}".format(string1[:half1+1], string2[:half2+1], string1[half1+1:], string2[half2:+1])

    else:
        return "ERROR"
    # print("string len {}".format(length_str1))    print line used for testing


def main():
    print("== ends ==")
    letters = input("Enter a string >>> ")
    # string = "testprogram"     hard code to test program
    print(ends(letters))

    print()

    print("== mix ==")
    # a = "test"
    # b = "mix"
    a = input("String A: ")
    b = input("String B: ")
    print(mix(a, b))

    print()

    print("== split it ==")
    # a = "abcdi"
    # b = "efgh"
    a = input("String A: ")
    b = input("String B: ")
    print(split(a, b))

if __name__ == "__main__":
    main()