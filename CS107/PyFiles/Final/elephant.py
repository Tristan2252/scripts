from sensor import Sensor
from tank import Tank


class Elephant(Tank):

    def __init__(self):
        Tank.tank_shape = [[4, 4], [5, 4], [5, 5], [-5, 5], [-5, 4], [-4, 4],
                           [-4, -4], [-5, -4], [-5, -5], [5, -5], [5, -4], [4, -5]]
        Tank.__init__(self)

        self.sensors = [Sensor(0, 20, 50, True),       # 0 Turret
                        Sensor(0, 20, 100, False),     # 1 Front
                        Sensor(20, 20, 100, False),    # 2 Front left
                        Sensor(340, 20, 100, False)]   # 3 Front right

        self._kill_count = 0
        self.tread_max = 30
        self.tread_accel = 30

    def attack(self):
        """
        movement the tank does if the turret is ready to fire and attack
        :return: None
        """
        if self.read_sensor(1):
            self.set_speed('l', 50)
            self.set_speed('r', 50)
        elif self.read_sensor(2):
            self.set_speed('l', 100)
        elif self.read_sensor(3):
            self.set_speed('r', 100)
        elif self.read_sensor(0):
            self.fire(True)
        else:
            self.set_speed('r', 20)
            self.set_speed('l', 20)

    def kill(self):
        """
        overrides kill function to add 3 lives to the tank
        :return: None
        """

        self._kill_count += 1  # adds one to kill count every time kill is called
        if self._kill_count == 3:
            Tank.kill(self)

    def ai(self, delta):
        """
        tank AI
        :param delta:
        :return: None
        """
        if self.turret_ready():
            self.attack()

        else:
            self.set_speed('r', 20)
            self.set_speed('l', 20)