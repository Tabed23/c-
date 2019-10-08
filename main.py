from abc import *


class Shape(ABC):

    def __init__(self, l=0, w=0):
        self._length = l
        self._width = w

    def get_length(self):
        return self._length

    def get_width(self):
        return self._width

    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return "{} {}".format(self._length, self._width)


class Square(Shape):

    def __init__(self, L=0, w=0):
        super().__init__(L, w)

    def area(self):
        return self.get_length() * self.get_length()


class Rectangle(Shape):

    def __init__(self, l=0, w=0):
        super().__init__(l, w)

    def area(self):
        return self.get_length() * self.get_width()


class Triangle(Shape):

    def __init__(self, l=0, w=0):
        super().__init__(l, w)

    def area(self):
        return 1 / 2 * self.get_length() * self.get_width()


s = Rectangle(2, 5)


print(s.area())
