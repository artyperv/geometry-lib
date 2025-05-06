import argparse
from geometry.shapes import Circle, Triangle
from geometry.utils import calculate_area


def main():
    parser = argparse.ArgumentParser(description="Geometry Area Calculator")

    subparsers = parser.add_subparsers(dest="shape", required=True)

    # Circle
    circle_parser = subparsers.add_parser("circle", help="Calculate area of a circle")
    circle_parser.add_argument("radius", type=float, help="Radius of the circle")

    # Triangle
    triangle_parser = subparsers.add_parser("triangle", help="Calculate area of a triangle")
    triangle_parser.add_argument("a", type=float, help="Side a")
    triangle_parser.add_argument("b", type=float, help="Side b")
    triangle_parser.add_argument("c", type=float, help="Side c")

    args = parser.parse_args()

    if args.shape == "circle":
        shape = Circle(args.radius)
    elif args.shape == "triangle":
        shape = Triangle(args.a, args.b, args.c)
        print(f"Right-angled? {shape.is_right_triangle()}")
    else:
        raise ValueError("Unsupported shape")

    area = calculate_area(shape)
    print(f"Area: {area:.2f}")