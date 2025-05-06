from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def __repr__(self):
        return f"Circle(radius={self.radius})"


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        sides = sorted([a, b, c])
        if any(side <= 0 for side in sides):
            raise ValueError("All sides must be positive")
        if sides[0] + sides[1] <= sides[2]:
            raise ValueError("Triangle inequality violated")

        self.a, self.b, self.c = sides

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_triangle(self) -> bool:
        return math.isclose(self.a ** 2 + self.b ** 2, self.c ** 2)

    def __repr__(self):
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"