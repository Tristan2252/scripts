from sensor import Sensor
from tank import Tank


class Mouse(Tank):

    def __init__(self):

        Tank.tank_shape = [[1, 1], [1, 2], [2, 2], [-2, 2], [-2, 1], [-1, 1],
                           [-1, -1], [-2, -1], [-2, -2], [2, -2], [2, -1], [1, -2]]

        Tank.__init__(self)
        self.sensors = [Sensor(0, 20, 50, True),      # 0 Turret
                        Sensor(90, 90, 100, False),   # 1 Left
                        Sensor(180, 90, 100, False),  # 2 Back
                        Sensor(270, 90, 100, False),  # 3 Right
                        Sensor(0, 20, 100, False),    # 4 Front
                        Sensor(20, 20, 100, False),   # 5 Front left
                        Sensor(340, 20, 100, False)]  # 6 Front right

        self._kill_count = 0
        self.tread_accel = 80
        self.tread_max = 80

    def avoid(self):
        """
        movement to avoid tanks that come in contact with side sensors
        and back sensor
        :return: None
        """
        if self.read_sensor(2):
            self.set_speed('l', 0)
            self.set_speed('r', 0)
            self.set_speed('l', 80)
            self.set_speed('r', 80)

        elif self.read_sensor(1):
            self.set_speed('l', 0)
            self.set_speed('r', 0)
            self.set_speed('r', 80)
            self.set_speed('l', 60)
        elif self.read_sensor(3):
            self.set_speed('l', 0)
            self.set_speed('r', 0)
            self.set_speed('l', 80)
            self.set_speed('r', 60)

    def ai(self, delta):
        """
        tank AI
        :param delta:
        :return: None
        """
        if self.read_sensor(0):
            self.fire(True)
        elif self.read_sensor(5):     # helps narrow down target
            self.set_speed('l', 0)
            self.set_speed('r', -70)
        elif self.read_sensor(6):     # "  "    " "    " "
            self.set_speed('l', 0)
            self.set_speed('r', 70)
        else:
            self.avoid()