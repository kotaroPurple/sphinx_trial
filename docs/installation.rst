Installation
============

Requirements
------------

* Python 3.13 or higher
* uv package manager

Installing sphinx-trial
------------------------

1. Clone the repository:

.. code-block:: bash

   git clone <repository-url>
   cd sphinx-trial

2. Create a virtual environment:

.. code-block:: bash

   uv venv

3. Install the library in editable mode:

.. code-block:: bash

   uv pip install -e .

4. (Optional) Install with documentation dependencies:

.. code-block:: bash

   uv pip install -e ".[docs]"

Verification
------------

Verify the installation by running:

.. code-block:: python

   from sphinx_trial import hello
   print(hello())  # Should print: Hello from sphinx-trial!

Running Examples
----------------

The library comes with comprehensive examples:

.. code-block:: bash

   # Run all examples
   uv run python run_examples.py

   # Run individual examples
   uv run python example/basic_usage.py
   uv run python example/math_examples.py
   uv run python example/text_examples.py
   uv run python example/utils_examples.py
   uv run python example/advanced_usage.py