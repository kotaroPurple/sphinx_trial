Tutorial
========

This tutorial will guide you through the main features of sphinx-trial.

Getting Started
---------------

First, make sure you have installed sphinx-trial following the :doc:`installation` guide.

Math Module
-----------

The math module provides calculator and geometry functionality.

Calculator
~~~~~~~~~~

.. code-block:: python

   from sphinx_trial.math import Calculator

   calc = Calculator()
   
   # Basic operations
   result = calc.add(10, 5)        # 15
   result = calc.subtract(10, 5)   # 5
   result = calc.multiply(10, 5)   # 50
   result = calc.divide(10, 5)     # 2.0

   # Error handling
   try:
       calc.divide(10, 0)
   except ZeroDivisionError as e:
       print(f"Error: {e}")

Geometry
~~~~~~~~

.. code-block:: python

   from sphinx_trial.math import Circle, Rectangle

   # Circle calculations
   circle = Circle(5)
   area = circle.area()                # 78.54
   circumference = circle.circumference()  # 31.42

   # Rectangle calculations
   rect = Rectangle(4, 6)
   area = rect.area()          # 24
   perimeter = rect.perimeter()  # 20

Text Module
-----------

The text module provides formatting and validation utilities.

Text Formatting
~~~~~~~~~~~~~~~

.. code-block:: python

   from sphinx_trial.text import TextFormatter

   formatter = TextFormatter()
   
   # Capitalize words
   text = formatter.capitalize_words("hello world")  # "Hello World"
   
   # Remove spaces
   text = formatter.remove_spaces("hello world")     # "helloworld"
   
   # Truncate text
   text = formatter.truncate("Very long text", 10)   # "Very lo..."

Text Validation
~~~~~~~~~~~~~~~

.. code-block:: python

   from sphinx_trial.text import is_email, is_phone, is_url

   # Email validation
   valid = is_email("user@example.com")    # True
   valid = is_email("invalid-email")       # False

   # Phone validation
   valid = is_phone("123-456-7890")        # True
   valid = is_phone("invalid")             # False

   # URL validation
   valid = is_url("https://example.com")   # True
   valid = is_url("invalid-url")           # False

Utils Module
------------

The utils module provides logging and configuration management.

Logging
~~~~~~~

.. code-block:: python

   from sphinx_trial.utils import SimpleLogger

   # Default logger
   logger = SimpleLogger()
   logger.info("This is an info message")
   logger.warning("This is a warning")
   logger.error("This is an error")

   # Named logger
   app_logger = SimpleLogger("MyApp")
   app_logger.info("Application started")

Configuration
~~~~~~~~~~~~~

.. code-block:: python

   from sphinx_trial.utils import Config

   config = Config()
   
   # Set values
   config.set("app_name", "MyApp")
   config.set("debug", True)
   
   # Get values
   name = config.get("app_name")           # "MyApp"
   debug = config.get("debug")             # True
   timeout = config.get("timeout", 30)    # 30 (default)
   
   # Check existence
   exists = config.has("app_name")         # True

Advanced Usage
--------------

You can combine multiple modules for more complex functionality:

.. code-block:: python

   from sphinx_trial.math import Calculator, Circle
   from sphinx_trial.text import TextFormatter, is_email
   from sphinx_trial.utils import SimpleLogger, Config

   # Setup
   logger = SimpleLogger("MyApp")
   config = Config()
   config.set("precision", 2)

   # Calculate and log results
   calc = Calculator()
   result = calc.add(10.567, 5.432)
   
   precision = config.get("precision")
   rounded_result = round(result, precision)
   
   logger.info(f"Calculation result: {rounded_result}")

Next Steps
----------

* Explore the :doc:`examples` for more comprehensive usage patterns
* Check the :doc:`api/math`, :doc:`api/text`, and :doc:`api/utils` for detailed API documentation