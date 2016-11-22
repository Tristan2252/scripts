import random
from sensor import Sensor
from tank import Tank


class Charger(Tank):

    def __init__(self):
        Tank.__init__(self)
        self.sensors = [Sensor(0, 20, 100, False),     # 0 Front
                        Sensor(20, 20, 100, False),    # 1 Front left
                        Sensor(340, 20, 100, False),   # 2 Front right
                        Sensor(0, 20, 50, True),       # 3 turret range
                        Sensor(90, 120, 100, False),   # 4 Left
                        Sensor(180, 60, 100, False),   # 5 Back
                        Sensor(270, 120, 100, False),  # 6 Right
                        Sensor(0, 180, 80, False)]     # 7 Front Shield
        self.clockwise = random.random() < 0.5

    def attack(self):
        """
        movement the tank does if the turret is ready to fire and attack
        :return: None
        """

        if self.read_sensor(0) and self.read_sensor(3):
            """
            if the target is within the front sensor and within range of the
            turret the tank will fire
            """
            self.fire(True)

        elif self.read_sensor(1):  # Front left
            """
            turns the tanks left if Front left sensor detects something in order
            to line up the target.
            """
            self.set_speed('l', 0)
            self.set_speed('r', -70)
            # faster than left and right in order to counter unnecessary
            # high speed spinning
        elif self.read_sensor(2):  # Front right
            self.set_speed('l', 0)
            self.set_speed('r', 70)

        elif self.read_sensor(4) or self.read_sensor(5):  # Left or Back
            self.set_speed('l', 0)
            self.set_speed('r', -70)

        elif self.read_sensor(6):  # Right
            self.set_speed('l', 0)
            self.set_speed('r', 50)

        else:
            self.set_speed('l', 30)
            self.set_speed('r', 25)

    def normal_move(self):
        """
        movement the tank does when the turret is not ready to fire
        :return: None
        """

        if self.read_sensor(5):  # Back
            self.set_speed('l', 50)
            self.set_speed('r', 50)
        elif self.read_sensor(7):  # Front
            self.set_speed('l', -50)
            self.set_speed('r', -50)

        else:
            self.set_speed('l', 30)
            self.set_speed('r', 25)

    def ai(self, delta):
        """
        tank AI
        :param delta:
        :return: None
        """

        if self.turret_ready():
            self.attack()

        else:
            self.normal_move()