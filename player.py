class Player:
    def __init__(self, pos):
        self._x, self._y = pos
        self._angle = 0

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y

    @property
    def pos(self):
        return self._x, self._y
    
    @property
    def angle(self):
        return self._angle
    
    @x.setter
    def x(self, x):
        self._x = x

    @y.setter
    def y(self, y):
        self._y = y

    @pos.setter
    def pos(self, x, y):
        self.x = x
        self.y = y

    @angle.setter
    def angle(self, value):
        self._angle = value
