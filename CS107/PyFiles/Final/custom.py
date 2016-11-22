from sensor import Sensor
from tank import Tank
import random


class Custom(Tank):

    def __init__(self):
        Tank.__init__(self)
        self.sensors = [Sensor(0, 20, 100, False),     # 0 Front
                        Sensor(20, 20, 100, False),    # 1 Front left
                        Sensor(340, 20, 100, False),   # 2 Front right
                        Sensor(0, 20, 110, True),      # 3 turret range
                        Sensor(90, 120, 100, False),   # 4 Left
                        Sensor(180, 60, 100, False),   # 5 Back
                        Sensor(270, 120, 100, False),  # 6 Right
                        Sensor(0, 180, 80, False),     # 7 Front Shield
                        Sensor(180, 180, 80, False)]   # 8 Back Shield
        self._kill_count = 0
        self.turret_range = 110
        self.tread_accel = 80
        self.tread_max = 80
        self.cooldown = 0

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
            direct = random.choice(range(10))  # random direction to go
            direct2 = random.choice(range(10))
            self.set_speed('l', direct * 10)
            self.set_speed('r', direct2 * 10)

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
            direct = random.choice(range(10))
            direct2 = random.choice(range(10))
            self.set_speed('l', direct * 10)
            self.set_speed('r', direct2 * 10)

    def be_careful(self):
        """
        function includes directions to keep the tank away from
        in coming enemies that it is unable to hit
        :return:
        """

        if self.read_sensor(7):
            self.set_speed('l', -50)
            self.set_speed('r', -50)
        elif self.read_sensor(8):
            self.set_speed('l', 50)
            self.set_speed('r', 50)

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
            direct = random.choice(range(5))
            direct2 = random.choice(range(5))
            self.set_speed('l', direct * 10)
            self.set_speed('r', direct2 * 10)

    def kill(self):
        """
        overrides kill function to add 3 lives to the tank
        :return: None
        """

        self._kill_count += 1  # adds one to kill count every time kill is called
        print(self._kill_count)  # shows life of tank
        if self._kill_count == 3:
            Tank.kill(self)

    def ai(self, delta):
        """
        tank AI
        :param delta:
        :return: None
        """
        if self._kill_count >= 2:  # regenerative health when only one life left
            self._kill_count -= 0.2

        if self.turret_ready() and self._kill_count < 2:
            self.attack()

        elif self.turret_ready() and self._kill_count > 2:  # if health is low be careful
            self.be_careful()

        else:
            self.normal_move()