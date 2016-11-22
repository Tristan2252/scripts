import turtle as tr


def open_file(file_name):
    """
    attempts to open a file as read and creates a list of the files
    contents, then splits the file by '\n' and returns the list. if
    the file is not found, user is asked to try another file name.
    :param file_name: str  # the name of the file
    :return: []            # a list of the files contents, split by line
    """
    while True:
        try:
            with open(file_name, "r") as file:
                direct_list = file.read()
                split_file = direct_list.split("\n")
                return split_file
        except FileNotFoundError:
            print("\n === File not found === ")
            file_name = input("Enter a different file name: ")


def split(turtle, angle):
    """
    gives the look of the turtle splitting by cloning the original
    turtle and then turning it right a given angle (opposite of the
    original turtle)
    :param turtle: turtle
    :param angle: int() # angle the turtle will turn
    :return: turtle     # the new cloned turtle
    """
    turtle1 = turtle.clone()
    turtle1.right(angle)
    return turtle1


def run_turtle(direct, turtles):
    """
    function that runs the turtles commands by iterating through the list
    of strings and testing if it is equal to the designated command, if so
    the command is ran. At the end the new list of new turtles are added to
    the list of turtles.
    :param direct: []   # list of directions from the file
    :param turtles: []  # list of turtles that have been created
    :return: None
    """
    for i in direct:
        cmd = i.split()
        print(cmd)

        new_turt = []
        for turt in turtles:
            if cmd[0] == "forward":
                value = int(cmd[1])
                turt.forward(value)
            if cmd[0] == "left":
                value = int(cmd[1])
                turt.left(value)
            if cmd[0] == "right":
                value = int(cmd[1])
                turt.right(value)
            if cmd[0] == "split":
                value = int(cmd[1])
                new_turt.append(split(turt, value))
            if cmd[0] not in ["forward", "left", "right", "split"]:  # prints error if cmd doesnt exist
                print(" === Invalid Command === ")
            else:
                pass
        turtles += new_turt  # adds the list of new turtles to to turtles list


def main():

    file_name = input("\nEnter the name of the file containing the directions: ")
    direct = open_file(file_name)

    turtles = []
    t1 = tr.Turtle()  # firs turtle created to start the loop
    turtles.append(t1)  # added to the turtle list
    print("\n{}\n".format(turtles))
    run_turtle(direct, turtles)


if __name__ == '__main__':
    main()