import math


class Tire(object):

    def __init__(self, tractioon, radius):
        self.traction = tractioon
        self.radius = radius

    def circumference(self):
        """
        finds the circumference of the tire by multiplying
        the diameter by pi
        :return: int
        """
        return self.diamiter() * math.pi

    def diamiter(self):
        """
        finds the diameter of the dire
        :return: int
        """
        return self.radius * 2


def main():
    pass

if __name__ == '__main__':
    main()