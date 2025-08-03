"""Math module usage examples."""

from sphinx_trial.math import Calculator, Circle, Rectangle

def calculator_example():
    """Demonstrate Calculator usage."""
    print("=== Calculator Examples ===")
    calc = Calculator()
    
    print(f"Addition: 15 + 25 = {calc.add(15, 25)}")
    print(f"Subtraction: 100 - 30 = {calc.subtract(100, 30)}")
    print(f"Multiplication: 7 * 8 = {calc.multiply(7, 8)}")
    print(f"Division: 20 / 4 = {calc.divide(20, 4)}")
    
    # Error handling
    try:
        calc.divide(10, 0)
    except ZeroDivisionError as e:
        print(f"Error caught: {e}")

def geometry_examples():
    """Demonstrate geometry classes."""
    print("\n=== Geometry Examples ===")
    
    # Circle examples
    circle = Circle(3)
    print(f"Circle (radius=3):")
    print(f"  Area: {circle.area():.2f}")
    print(f"  Circumference: {circle.circumference():.2f}")
    
    # Rectangle examples
    rect = Rectangle(4, 6)
    print(f"Rectangle (4x6):")
    print(f"  Area: {rect.area()}")
    print(f"  Perimeter: {rect.perimeter()}")

def main():
    """Run all math examples."""
    calculator_example()
    geometry_examples()

if __name__ == "__main__":
    main()