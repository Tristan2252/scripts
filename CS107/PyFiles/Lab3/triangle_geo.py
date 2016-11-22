import math


def area(height, base):
    area = height * base
    print("The area of the triangle is {}".format(area))


def par(height, base):
    perimeter = height + base + math.sqrt(height ** 2 + base ** 2)
    print("The perimeter of the triangle {}".format(perimeter))
