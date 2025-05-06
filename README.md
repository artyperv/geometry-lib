# Geometry Library

A Python library for calculating the area of geometric shapes (circle and triangle).

## Features

- Calculate circle area by radius
- Calculate triangle area by three sides
- Determine if a triangle is right-angled
- Unified interface for all shapes

## Installation

```bash
pip install git+https://github.com/artyperv/geometry-lib.git
```

## Usage

```python
from geometry.shapes import Circle, Triangle
from geometry.utils import calculate_area

circle = Circle(3)
triangle = Triangle(3, 4, 5)

print(f"Circle area: {calculate_area(circle):.2f}")
print(f"Triangle area: {calculate_area(triangle):.2f}")
print(f"Is triangle right-angled? {triangle.is_right_triangle()}")
```

#### CLI

```bash
geometry-cli circle 3
# Output: Area: 28.27

geometry-cli triangle 3 4 5
# Output: Right-angled? True
#         Area: 6.00
```

## Testing
```bash
pytest
```

