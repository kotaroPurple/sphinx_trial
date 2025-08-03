"""Basic usage example of sphinx-trial library."""

from sphinx_trial import hello, Calculator, Circle, TextFormatter, SimpleLogger

def main():
    """Demonstrate basic usage of the library."""
    print("=== Basic Usage Example ===")
    
    # Hello function
    print(f"Greeting: {hello()}")
    
    # Calculator
    calc = Calculator()
    print(f"Calculator: 10 + 5 = {calc.add(10, 5)}")
    
    # Circle
    circle = Circle(5)
    print(f"Circle (radius=5): area = {circle.area():.2f}")
    
    # Text formatter
    formatter = TextFormatter()
    text = "hello world"
    print(f"Formatted text: '{formatter.capitalize_words(text)}'")
    
    # Logger
    logger = SimpleLogger("example")
    logger.info("Basic usage example completed")

if __name__ == "__main__":
    main()