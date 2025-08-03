sphinx-trial documentation
==========================

A sample Python library demonstrating multiple modules with comprehensive documentation.

sphinx-trial provides three main modules:

* **math**: Calculator and geometry classes for mathematical operations
* **text**: Text formatting and validation utilities  
* **utils**: Logging and configuration management tools

Quick Start
-----------

Install the library:

.. code-block:: bash

   uv venv
   uv pip install -e .

Basic usage:

.. code-block:: python

   from sphinx_trial import Calculator, Circle, TextFormatter

   # Math operations
   calc = Calculator()
   result = calc.add(10, 5)  # 15

   # Geometry
   circle = Circle(5)
   area = circle.area()  # 78.54

   # Text formatting
   formatter = TextFormatter()
   text = formatter.capitalize_words("hello world")  # "Hello World"

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: User Guide:

   installation
   tutorial
   examples

.. toctree::
   :maxdepth: 2
   :caption: API Reference:

   api/math
   api/text
   api/utils

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`