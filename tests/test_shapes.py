import pytest
from geometry.shapes import Circle, Triangle
from geometry.utils import calculate_area
import math


def test_circle_area():
    circle = Circle(1)
    assert math.isclose(circle.area(), math.pi)


def test_triangle_area():
    triangle = Triangle(3, 4, 5)
    assert math.isclose(triangle.area(), 6.0)


def test_triangle_is_right():
    triangle = Triangle(3, 4, 5)
    assert triangle.is_right_triangle() is True

    non_right_triangle = Triangle(4, 5, 6)
    assert non_right_triangle.is_right_triangle() is False


def test_invalid_circle():
    with pytest.raises(ValueError):
        Circle(-1)


def test_invalid_triangle_sides():
    with pytest.raises(ValueError):
        Triangle(1, 2, 10)


def test_calculate_area_polymorphic():
    shapes = [
        Circle(2),
        Triangle(3, 4, 5),
    ]
    areas = [calculate_area(s) for s in shapes]
    assert math.isclose(areas[0], math.pi * 4)
    assert math.isclose(areas[1], 6.0)
