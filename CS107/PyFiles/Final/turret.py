import random
import math
from sensor import Sensor
from tank import Tank


class Turret(Tank):

    def __init__(self):
        Tank.__init__(self)

        sensor_lst = []
        for i in range(20):  # makes 19 turrets
            sensor_lst.append(Sensor(i*20, 20, 100, False))
        sensor_lst.append(Sensor(0, 20, 50, True))  # Turret range sensor

        self.sensors = sensor_lst
        self.clockwise = random.random() < 0.5
        self.turret_speed = 360 / 180 * math.pi

    def ai(self, delta):
        """
        tank AI
        :param delta:
        :return: None
        """
        for i in range(20):
            if self.read_sensor(i):
                self.set_turret_target(i*20)
                if self.read_sensor(20) and self.turret_ready():
                    self.fire(True)