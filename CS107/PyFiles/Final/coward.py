import random
from sensor import Sensor
from tank import Tank


class Coward(Tank):

    def __init__(self):
        Tank.__init__(self)
        self.sensors = [Sensor(0, 90, 100, False),  # Front
                        Sensor(90, 90, 100, False),  # Left
                        Sensor(180, 90, 100, False),  # Back
                        Sensor(270, 90, 100, False)]  # Right

    def ai(self, delta):

        if self.read_sensor(0):
            self.set_speed('l', 0)
            self.set_speed('r', 0)
            self.set_speed('l', -150)
            self.set_speed('r', -150)
        elif self.read_sensor(2):
            self.set_speed('l', 0)
            self.set_speed('r', 0)
            self.set_speed('l', 150)
            self.set_speed('r', 150)

        elif self.read_sensor(1):
            self.set_speed('l', 0)
            self.set_speed('r', 0)
            self.set_speed('l', 100)
            self.set_speed('r', 60)
        elif self.read_sensor(3):
            self.set_speed('l', 0)
            self.set_speed('r', 0)
            self.set_speed('r', 100)
            self.set_speed('l', 80)
        else:
            self.set_speed('l', 0)
            self.set_speed('r', 0)
