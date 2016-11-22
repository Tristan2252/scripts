import turtle


class MyTurtle(turtle.Turtle):

    def forward(self, distance):
        """
        Overrides turtle function to move forward
        :param distance: int # distance for turtle to move
        :return: None
        """
        if distance >= 0:
            turtle.Turtle.forward(self, distance)

    def back(self, distance):
        """
        Overrides turtle function to move back
        :param distance: int # distance to move back
        :return: None
        """
        if distance >= 0:
            turtle.Turtle.back(self, distance)

    def left(self, angle):
        """
        Overrides turtle function to turn left
        :param angle: int # angle to turn turtle
        :return: None
        """
        if angle >= 0:
            turtle.Turtle.left(self, angle)

    def right(self, angle):
        """
        Overrides turtle function to turn right
        :param angle: int # angle to turn turtle
        :return: None
        """
        if angle >= 0:
            turtle.Turtle.right(self, angle)

    def regular_polygon(self, side_number, length):
        """
        Takes in side number and length and draws a polygon with x sides and
        x length of the sides
        :param side_number: int # number of sides
        :param length:  int # length of sides
        :return: None
        """
        angle = 180 * (side_number - 2)/side_number
        cnt = 0

        while cnt < side_number:
            turtle.Turtle.forward(self, length)
            turtle.Turtle.left(self, 180 - angle)
            cnt += 1


def main():
    t1 = MyTurtle()
    t2 = MyTurtle()
    t1.regular_polygon(5, 100)

    t2.left(72)
    t2.forward(160)
    t2.right(144)
    t2.forward(161)
    t2.right(144)
    t2.forward(164)
    t2.right(144)
    t2.forward(166)
    t2.left(36)
    t2.back(160)

if __name__ == '__main__':
    main()