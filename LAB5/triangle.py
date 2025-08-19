class Triangle:
    object_count = 0    # class variable for counting objects

    def __init__(self, a=1.0, b=None, c=None):
        if isinstance(a, Triangle):
            # clone constructor
            self.sideA = a.sideA
            self.sideB = a.sideB
            self.sideC = a.sideC
        elif b is None and c is None:  # one parameter-- equilateral
            self.sideA = self.sideB = self.sideC = a
        elif c is None:  # two parameters-- isosceles
            self.sideA = self.sideB = a
            self.sideC = b
        else:  # three parameters
            self.sideA = a
            self.sideB = b
            self.sideC = c
        Triangle.object_count += 1

    # properties for sideA
    @property
    def sideA(self):
        return self._sideA

    @sideA.setter
    def sideA(self, value):
        if value <= 0:
            raise ValueError("Side length must be positive")
        self._sideA = value

    # similarly for sideB
    @property
    def sideB(self):
        return self._sideB

    @sideB.setter
    def sideB(self, value):
        if value <= 0:
            raise ValueError("Side length must be positive")
        self._sideB = value

    # similarly for sideC
    @property
    def sideC(self):
        return self._sideC

    @sideC.setter
    def sideC(self, value):
        if value <= 0:
            raise ValueError("Side length must be positive")
        self._sideC = value

    def isRightAngled(self):
        sides = sorted([self.sideA, self.sideB, self.sideC])
        return abs(sides[2]**2 - (sides[0]**2 + sides[1]**2)) < 1e-9

    @staticmethod
    def objectcount():
        return Triangle.object_count

    def __str__(self):
        return f"Triangle({self.sideA}, {self.sideB}, {self.sideC})"
