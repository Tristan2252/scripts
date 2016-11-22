

def is_anagram(str1, str2):
    """
    function returns boolean value based on a test of if string 1 is = to string 3
    str1 and str2 : str
    """
    return sorted(str1) == sorted(str2)


def main():
    """
    Write a function that takes in two strings. If the strings are anagrams of one another, return
    True . If not, return False.
    """
    # str1 = "this is a test"
    # str2 = "is this a test"
    str1 = input("\nEnter string one: ")
    str2 = input("\nEnter string two: ")

    print(is_anagram(str1, str2))


if __name__ == '__main__':
    main()