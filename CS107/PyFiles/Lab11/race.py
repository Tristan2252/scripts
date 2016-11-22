import math
from car import Car


def main():
    radius = 1 / math.pi
    acceleration = 0.5
    max_speed = 100
    traction = 10
    hare = Car("Hare", acceleration, max_speed, traction, radius)

    radius = 1 / math.pi
    acceleration = 1
    max_speed = 120
    traction = 0
    rabbit = Car("Rabbit", acceleration, max_speed, traction, radius)

    print("\n"
          "--------------------- Car Settings -------------------\n"
          "Car\t Traction | Radius | Max Speed | Acceleration\n"
          "______________________________________________________")
    print(hare)
    print(rabbit)

    while True:
        option = input("\nWould you like to display results with fixed [time] or fixed [distance]: ")

        if option == "time":
            print("\n"
                  "--------------------- Results -----------------------\n"
                  "\t Time:\t      {}        {}\n"
                  "\t_________________________________"
                  "".format(hare.get_name(), rabbit.get_name()))

            for i in range(11):
                print("\t{:5.2f}     {:8.2f}      {:8.2f}"
                      .format(i, hare.travel_time(i), rabbit.travel_time(i)))
            break

        elif option == "distance":
            print("\n"
                  "--------------------- Results -----------------------\n"
                  "\t Distance:\t      {}        {}\n"
                  "\t_________________________________"
                  "".format(hare.get_name(), rabbit.get_name()))
            distance = 1462
            temp_dist = 0
            while distance >= temp_dist:
                print("\t{:5.2f}     {:8.2f}      {:8.2f}"
                      .format(temp_dist, hare.travel_distance(temp_dist),
                              rabbit.travel_distance(temp_dist)))
                temp_dist += 1

            break

        else:
            print("\nInvalid input, type time or distance")


if __name__ == '__main__':
    main()