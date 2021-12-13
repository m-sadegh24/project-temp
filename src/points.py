class point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __gt__(self, ob):
        return abs(self) > abs(ob)

    def __str__(self):
        return (f"{self.__class__.__name__}({self.x, self.y})")

    def __repr__(self):
        return (f"{self.__class__.__name__}({self.x, self.y})")

# print(point(3, 4))

class point_inf(object):
    def __init__(self, *args):
        self.args = args

    def __abs__(self):
        sum_v = sum([item ** 2 for item in self.args])
        return sum_v ** 0.5

    def __gt__(self, ob):
        return abs(self) > abs(ob)

    def __repr__(self):
        return (f"{self.__class__.__name__}{self.args}")

