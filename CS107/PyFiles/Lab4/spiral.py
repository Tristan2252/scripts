import turtle
'Use a for loop, range, and turtle to draw a spiral'


def spiral(angle):
    for i in range(100):  # the range at witch the loop will continue
        turtle.forward(i)  # uses i as the length the turtle travels
        turtle.left(angle)
        print("{}".format(i))
        i += 1  # increments i by 1


def main():
    print()
    spiral_angle = int(input('Enter the angle to draw the spiral with\n'
                             'Note the smaller the angle the lager the spiral: '))
    spiral(spiral_angle)  # calls spiral function
    # spiral(40)


if __name__ == "__main__":
    main()