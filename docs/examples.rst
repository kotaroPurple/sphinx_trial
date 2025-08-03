Examples
========

This section contains comprehensive examples demonstrating various features of sphinx-trial.

All example files are located in the ``example/`` directory and can be run directly:

.. code-block:: bash

   # Run all examples
   uv run python run_examples.py

   # Run individual examples
   uv run python example/basic_usage.py

Basic Usage
-----------

The basic usage example demonstrates the core functionality of each module:

.. literalinclude:: ../example/basic_usage.py
   :language: python
   :caption: example/basic_usage.py

Math Examples
-------------

Comprehensive examples of the math module:

.. literalinclude:: ../example/math_examples.py
   :language: python
   :caption: example/math_examples.py

Text Examples
-------------

Text processing and validation examples:

.. literalinclude:: ../example/text_examples.py
   :language: python
   :caption: example/text_examples.py

Utils Examples
--------------

Utility module demonstrations:

.. literalinclude:: ../example/utils_examples.py
   :language: python
   :caption: example/utils_examples.py

Advanced Usage
--------------

Advanced examples combining multiple modules:

.. literalinclude:: ../example/advanced_usage.py
   :language: python
   :caption: example/advanced_usage.py

Running the Examples
--------------------

To run any example:

1. Make sure sphinx-trial is installed:

   .. code-block:: bash

      uv pip install -e .

2. Run individual examples:

   .. code-block:: bash

      uv run python example/basic_usage.py
      uv run python example/math_examples.py
      uv run python example/text_examples.py
      uv run python example/utils_examples.py
      uv run python example/advanced_usage.py

3. Or run all examples at once:

   .. code-block:: bash

      uv run python run_examples.py

Expected Output
---------------

Each example produces output demonstrating the functionality:

* **basic_usage.py**: Shows greeting, calculation, geometry, formatting, and logging
* **math_examples.py**: Demonstrates calculator operations and geometry calculations
* **text_examples.py**: Shows text formatting and validation results
* **utils_examples.py**: Displays logging messages and configuration management
* **advanced_usage.py**: Combines multiple modules for real-world scenarios