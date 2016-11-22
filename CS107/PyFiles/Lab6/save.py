

def write_lines(file_name):
    """
    receives string from the user and writes the string to the file as a new line
    until the user enters nothing
    :param file_name: str
    :return: nothing
    """
    with open(file_name, "w") as file:
        line = input("\nEnter a line to add to {} ".format(file_name))
        while True:
            if line == "":
                break
            else:
                file.write("{}\n".format(line))
                line = input("Enter another line or ENTER to exit: ")


def get_file():
    """
    receives the file name from the user
    :return: str (name of the file)
    """
    file_name = input("\nEnter the name of the file: ")
    return file_name


def print_file(filename):
    """
    prints the file for the user after the user is done
    entering strings to be written to the file
    :param filename: str
    :return: str (contents of the file)
    """
    with open(filename, "r") as file:
        print("\n === File Contents ===\n")
        for line in file:
            print(line, end="")


def main():
    file_name = get_file()
    write_lines(file_name)
    print_file(file_name)

if __name__ == '__main__':
    main()