class Measurment(object):

    _magnitude = 0
    _error = 0

    def __init__(self, mag=0, err=0):
        self._magnitude = mag
        self._error = err

    def __str__(self):
        return "{} +/-{:0.3f}".format(self._magnitude, self._error)

    def set_magnitude(self, v):
        self.magnitude = v

    def set_error(self, v):
        self._error = v

    def get_magnitude(self):
        return self._magnitude

    def get_error(self):
        return self._error

    def __add__(self, a):
        nv = self._magnitude + a.get_magnitude()
        ne = (self._error**2 + a.get_error()**2)**0.5
        return Measurment(nv, ne)

    def __sub__(self, a):
        nv = self._magnitude - a.get_magnitude()
        ne = (self._error**2 + a.get_error()**2)**0.5
        return Measurment(nv, ne)


c1 = Measurment(10, 0.1)
c2 = Measurment(20, 0.1)

print(c1 + c2)
