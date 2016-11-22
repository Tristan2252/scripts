def get_info():
    """
    props the user for the file name and returns the file names
    if they are valid
    :return: ([], [])  # name of file one and two
    """
    while True:
        print("\nEnter the name of file 1")
        file1 = get_file()  # how can i get input from a function on the same line as print line?
        print("\nEnter the name of file 2")
        file2 = get_file()
        return file1, file2


def get_file():
    """
    gets input from the user and tests if the input is a
    valid file
    :return: str  # name of the file
    """
    name = input()
    while True:
        try:
            with open(name, "r"):
                return name
        except FileNotFoundError:
            name = input("'{}' is not found, enter another name: ".format(name))


def split_file(info):
    """
    opens the files as read and reads the lines as a list
    then returns the list
    :param info: ([], []) # tuple of the file names
    :return: [], []  # list of lines for files
    """
    with open(info[0], "r") as file:
        lines1 = file.readlines()
    with open(info[1], "r") as file:
        lines2 = file.readlines()
    return lines1, lines2


def find_diff(info):
    """
    find the difference between a tuple of two lists by iterating
    through the lines of file1 and comparing them to the lines in
    file2. if the lines are not the same they are added to list 1
    or list 2
    :param info: ([], [])  # file names
    :return: ([], [])  # lists of non common files
    """
    same_in_f1 = []  # final lists used to store strings that are not similar
    same_in_f2 = []
    file1 = info[0]  # sets file1 = to the first list
    file2 = info[1]
    for i, line in enumerate(file1):  # enumerate is used to get line numbers to compare files by line #
        if line == file2[i]:
            pass
        else:
            same_in_f1.append(line)
            same_in_f2.append(file2[i])
    return same_in_f1, same_in_f2


def main():
    info = get_info()
    print("\nFiles being tested: {}".format(info))

    contents = split_file(info)  # splits the file into two lists of strings
    diff = find_diff(contents)
    file1 = diff[0]  # assigns lists to their corresponding variable
    file2 = diff[1]

    print("\n === Compared by File ===")
    print(" -- Different lines in file: {} ".format(info[0]))
    for i in file1:
        print("> {}".format(i), end="")
    print(" -- Different lines in file: {} ".format(info[1]))
    for i in file2:
        print("> {}".format(i), end="")

    print("\n === Compared by Line === ")
    for i in range(round(len(file1) / 2)):
        print("> {}< {}"
              "-------------------------\n".format(file1[i], file2[i]), end="")
        print("> {}< {}"
              "-------------------------\n".format(file1[i+1], file2[i+1]), end="")


if __name__ == '__main__':
    main()