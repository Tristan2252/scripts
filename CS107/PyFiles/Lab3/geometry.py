import circle_geo
import rectangle_gio
import triangle_geo
import polygon_gio


def main():

    exit_program = False
    while not exit_program:
        print()

        option = input('--- OPTIONS --- type exit to quit \n'
                       ' Triangle        Rectangle       Polygon         Circle\n'
                       ' area            area            area            area\n'
                       ' hypotenuse      perimeter   exterior angle      circumference\n'
                       ' perimeter       diagonal    interior_angle\n'
                       '>>> ')
        print()

        if option == "Rectangle":
            option2 = input(">>> Rectangle >>> ")
            rectangle_width = int(input("Enter the width of the rectangle "))
            rectangle_height = int(input("Enter the height of the rectangle "))
            if option2 == "area":
                rectangle_gio.area(rectangle_height, rectangle_width)
            elif option2 == "perimeter":
                rectangle_gio.per(rectangle_height, rectangle_width)

        elif option == "Circle":
            option2 = input(">>> Circle >>> ")
            circle_radius = int(input("Enter the radius of your circle "))
            if option2 == "area":
                circle_geo.area(circle_radius)
            elif option2 == "circumference":
                circle_geo.circumf(circle_radius)

        elif option == "Triangle":
            option2 = input(">>> Triangle >>> ")
            triangle_height = int(input("Enter the height of the triangle "))
            triangle_base = int(input("Enter the base length of the triangle "))
            if option2 == "area":
                triangle_geo.area(triangle_height, triangle_base)
            elif option2 == "perimeter":
                triangle_geo.par(triangle_height, triangle_base)

        elif option == "Polygon":
            option2 = input(">>> Polygon >>> ")
            polygon_side = int(input("Enter the number of sides in the polygon "))
            polygon_length = int(input("Enter the length of the polygon sides "))
            if option2 == "exterior angle":
                polygon_gio.exter(polygon_side)
            elif option2 == "interior angle":
                polygon_gio.inter(polygon_side)
            elif option2 == "area":
                polygon_gio.area(polygon_side, polygon_length)

        elif option == "exit":
            exit_program = True

        else:
            print("invalid input")
            print()

if __name__ == "__main__":
    main()