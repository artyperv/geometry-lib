from .shapes import Shape


def calculate_area(shape: Shape) -> float:
    if not isinstance(shape, Shape):
        raise TypeError("Object must be an instance of Shape")
    return shape.area()
