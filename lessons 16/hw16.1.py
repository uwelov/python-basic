from functools import total_ordering


@total_ordering
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle({self.width} x {self.height}, area: {self.area})"

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area == other.area

    def __lt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area < other.area

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        new_area = self.area + other.area
        return Rectangle(self.width, new_area / self.width)

    def __mul__(self, n):
        if not isinstance(n, (int, float)):
            return NotImplemented
        new_area = self.area * n
        return Rectangle(self.width, new_area / self.width)

    def __rmul__(self, n):
        return self.__mul__(n)


# Перевірка
r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)

print(r1)
print(r2)

assert (r1 < r2) is True
assert (r1 > r2) is False
assert (r1 == Rectangle(4, 2)) is True

r3 = r1 + r2
print(r3)
assert isinstance(r3, Rectangle) is True
assert r3.area == 26, "8 + 18 = 26"

r4 = r1 * 3
print(r4)
assert isinstance(r4, Rectangle) is True
assert r4.area == 24, "8 * 3 = 24"

print('Ok')