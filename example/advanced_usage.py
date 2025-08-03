"""Advanced usage example combining multiple modules."""

from sphinx_trial.math import Calculator, Circle
from sphinx_trial.text import TextFormatter, is_email
from sphinx_trial.utils import SimpleLogger, Config

def calculate_and_format_results():
    """Combine math and text modules for formatted calculations."""
    print("=== Advanced Usage: Calculation Report ===")
    
    logger = SimpleLogger("CalculationApp")
    formatter = TextFormatter()
    calc = Calculator()
    
    logger.info("Starting calculation report")
    
    # Perform calculations
    results = {
        "addition": calc.add(123.45, 67.89),
        "multiplication": calc.multiply(15, 8),
        "division": calc.divide(100, 3)
    }
    
    # Format and display results
    for operation, result in results.items():
        formatted_op = formatter.capitalize_words(operation)
        if isinstance(result, float):
            print(f"{formatted_op}: {result:.2f}")
        else:
            print(f"{formatted_op}: {result}")
    
    logger.info("Calculation report completed")

def geometry_calculator_with_config():
    """Use config to manage geometry calculations."""
    print("\n=== Advanced Usage: Configurable Geometry Calculator ===")
    
    config = Config()
    logger = SimpleLogger("GeometryApp")
    formatter = TextFormatter()
    
    # Set configuration
    config.set("default_radius", 5.0)
    config.set("precision", 3)
    config.set("show_formulas", True)
    
    logger.info("Geometry calculator initialized")
    
    # Create circle with configured radius
    radius = config.get("default_radius")
    circle = Circle(radius)
    precision = config.get("precision")
    
    # Calculate and format results
    area = round(circle.area(), precision)
    circumference = round(circle.circumference(), precision)
    
    print(f"Circle with radius {radius}:")
    print(f"  Area: {area}")
    print(f"  Circumference: {circumference}")
    
    if config.get("show_formulas"):
        print("  Formulas used:")
        print("    Area = π × r²")
        print("    Circumference = 2 × π × r")
    
    logger.info(f"Calculated circle properties for radius {radius}")

def user_data_processor():
    """Process user data with validation and logging."""
    print("\n=== Advanced Usage: User Data Processor ===")
    
    logger = SimpleLogger("UserProcessor")
    formatter = TextFormatter()
    
    # Sample user data
    users = [
        {"name": "john doe", "email": "john@example.com"},
        {"name": "jane smith", "email": "invalid-email"},
        {"name": "bob johnson", "email": "bob@test.org"}
    ]
    
    logger.info(f"Processing {len(users)} users")
    
    valid_users = []
    for user in users:
        # Format name
        formatted_name = formatter.capitalize_words(user["name"])
        
        # Validate email
        if is_email(user["email"]):
            valid_users.append({
                "name": formatted_name,
                "email": user["email"]
            })
            logger.info(f"Valid user: {formatted_name}")
        else:
            logger.warning(f"Invalid email for user: {formatted_name}")
    
    print(f"Processed {len(valid_users)} valid users:")
    for user in valid_users:
        print(f"  - {user['name']} ({user['email']})")

def main():
    """Run all advanced examples."""
    calculate_and_format_results()
    geometry_calculator_with_config()
    user_data_processor()

if __name__ == "__main__":
    main()