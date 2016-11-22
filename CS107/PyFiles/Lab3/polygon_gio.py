import math


def exter(side_number):
    exterior = 180 * (side_number - 2) / side_number
    exterior_sum = exterior * side_number
    print("The exterior angel of the polygon is {}".format(exterior))
    print("The sum of the exterior angles is {}".format(exterior_sum))


def inter(side_number):
    interior = (side_number - 2 / side_number) * 180
    print("The interior angel of the polygon is {}".format(interior))


def area(side_number, side_length):
    apothem = side_length / (2 * math.tan(180 / side_number))
    perimeter = side_length * side_number
    area = 0.5 * perimeter * apothem
    print("The area of the polygon is {}".format(area))
