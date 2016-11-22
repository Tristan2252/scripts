

def get_info():
    """
    gets input from the user for what file and word to find.
    if the file is not found the error is accepted and the user
    prompted to enter a valid input
    :return: (str, str) # consists of the name of the file and a string to find
    """
    while True:
        file_name = input("Enter the name of the file: ")
        try:  # attempts to open file to check if it exists
            with open(file_name, "r"):
                string = input("Enter a word to count: ")
                return file_name, string
                break
        except FileNotFoundError:
            print("{} is not an existing file".format(file_name))


def word_cnt(file_name, string):
    """
    takes in file name and string to find, opens the file as read, then reads the
    file and counts the number of time the string occurs in the file
    :param file_name: str   # name of the file
    :param string: str      # string to find
    :return: int            # number of occurrences
    """
    with open(file_name, "r") as file1:
        words = file1.read()
        occurrence = words.count(string)
    return occurrence


def main():
    info = get_info()  # info[0] = file name ---- info[1] = string to find
    print("\nFilename: {} | Word to find: '{}'".format(info[0], info[1]))
    counted = word_cnt(info[0], info[1])
    print("\n'{}' is in the file {} times".format(info[1], counted))


if __name__ == '__main__':
    main()
