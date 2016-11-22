import math
from engine import Engine
from tire import Tire

debug = False


class Car(object):
    def __init__(self, name, acceleration, max_speed, traction, radius):
        self._name = name
        self._acceleration = acceleration
        self._max_speed = max_speed
        self._traction = traction
        self._radius = radius
        self._engine = Engine(acceleration, max_speed)
        self._tire = Tire(traction, radius)

    def __str__(self):
        """
        prints out the car settings in a table fromat
        :return: str
        """
        return "{}\t | {:6.1f} | {:6.2f} | {:9.1f} | {:11.1f} |"\
            .format(self._name, self._traction,
                    self._radius, self._max_speed,
                    self._acceleration)

    def get_name(self):
        """
        returns the name of the car
        :return: str
        """
        return self._name

    def engine_speed(self, time):
        """
        calls the speed function in engine and returns the engine speed
        :param time: int
        :return: int
        """
        return self._engine.speed(time)

    def ideal_speed(self, time):
        """
        finds the ideal speed of the car by multiplying the engine speed
        by the tire circumference
        :param time: int
        :return: int
        """
        engine_speed = self.engine_speed(time)
        tire_cir = self._tire.circumference()

        return engine_speed * tire_cir

    def speed(self, time):
        """
        finds the actual speed of the car using the equation
        car_speed = pre_speed + (traction + car_accel) / 2
        :param time: int
        :return: int
        """

        if time == 0:
            return 0
        else:
            car_speed = self.ideal_speed(time)
            pre_speed = self.speed(time - 1)
            car_accel = car_speed - pre_speed
            traction = self._tire.traction

            if car_accel >= traction:
                car_speed = pre_speed + (traction + car_accel) / 2
        return car_speed

    def travel_time(self, time):
        """
        finds the distance the car travels in a specified time
        :param time: int
        :return: int
        """
        distance = 0
        for i in range(time):

            distance += self.speed(i)

        return distance

    def travel_distance(self, dist):
        """
        finds the distance a cat travels in a given time
        :param dist: int
        :return: int
        """

        time = 0
        temp_dist = 0
        while True:
            if temp_dist >= dist:
                return time
            else:
                temp_dist += self.speed(time)
            time += 1

if __name__ == '__main__':
    if debug:
        radius = 1 / math.pi
        acceleration = 0.5
        max_speed = 100
        traction = 10
        here = Car("hare", acceleration, max_speed, traction, radius)

        print(here.travel_time(10))
        print(here.travel_distance(1462))