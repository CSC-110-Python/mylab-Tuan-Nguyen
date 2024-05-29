import math


def rectangle_area(length, width):
    return length * width


def circle_area(radius):
    return math.pi * radius ** 2


def sphere_volume(radius):
    return (4 / 3) * math.pi * radius ** 3


def to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def quadratic(a=1, b=1, c=1):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root,
    else:
        return "No real roots"


def distance(x1=1, y1=1, x2=4, y2=5):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def print_all_info():
    print("Rectangle Area:", rectangle_area(12, 13), "square units")
    print("Circle Area:", circle_area(5), "square units")
    print("Sphere Volume:", sphere_volume(9), "cubic units")
    print("100 Fahrenheit to Celsius:", to_celsius(100), "degrees Celsius")
    print("0 Fahrenheit to Celsius:", to_celsius(0), "degrees Celsius")
    print("212 Celsius to Fahrenheit:", to_fahrenheit(212), "degrees Fahrenheit")
    print("32 Celsius to Fahrenheit:", to_fahrenheit(32), "degrees Fahrenheit")
    print("Quadratic Roots:", quadratic())
    print("Distance between (2, 5) and (7, 17):", distance(2, 5, 7, 17))


def test_functions():
    print("Testing rectangle_area(12, 13):", rectangle_area(12, 13) == 156)
    print("Testing circle_area(5):", circle_area(5) == math.pi * 25)
    print("Testing sphere_volume(9):", sphere_volume(9) == (4 / 3) * math.pi * 729)
    print("Testing to_celsius(100):", to_celsius(100) == (100 - 32) * 5 / 9)
    print("Testing to_fahrenheit(0):", to_fahrenheit(0) == 32)
    print("Testing quadratic(1, -3, 2):", quadratic(1, -3, 2) == (2.0, 1.0))
    print("Testing distance(2, 5, 7, 17):", distance(2, 5, 7, 17) == math.sqrt((7 - 2) ** 2 + (17 - 5) ** 2))


if __name__ == "__main__":
    print_all_info()
    test_functions()
