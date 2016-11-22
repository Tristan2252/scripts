
class Engine(object):

    def __init__(self, acceleration, max_speed):
        self._max_speed = max_speed
        self._acceleration = acceleration

    def speed(self, time):
        """
        finds the speed of the engine using the equation
        new_speed = old_speed + acceleration * (max_speed - old_speed)
        :param time: int
        :return: int
        """
        new_speed = 0
        acceleration = self._acceleration
        max_speed = self._max_speed

        for i in range(time):
            old_speed = new_speed
            new_speed = old_speed + acceleration * (max_speed - old_speed)

        return new_speed


def main():
    pass

if __name__ == '__main__':
    main()