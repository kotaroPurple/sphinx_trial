# sphinx-trial Examples

This directory contains usage examples for the sphinx-trial library.

## Examples

### 1. basic_usage.py
Basic introduction to the library's main features:
- Hello function
- Calculator usage
- Circle geometry
- Text formatting
- Simple logging

### 2. math_examples.py
Comprehensive examples of the math module:
- Calculator operations (add, subtract, multiply, divide)
- Error handling for division by zero
- Circle area and circumference calculations
- Rectangle area and perimeter calculations

### 3. text_examples.py
Text processing and validation examples:
- Text formatting (capitalize, remove spaces, truncate)
- Email validation
- Phone number validation
- URL validation

### 4. utils_examples.py
Utility module demonstrations:
- Simple logging with different levels
- Named loggers
- Configuration management
- Getting/setting config values

### 5. advanced_usage.py
Advanced examples combining multiple modules:
- Calculation report with formatting and logging
- Configurable geometry calculator
- User data processor with validation

## Running Examples

First, install the library in editable mode:

```bash
uv venv
uv pip install -e .
```

To run individual examples:

```bash
uv run python example/basic_usage.py
uv run python example/math_examples.py
uv run python example/text_examples.py
uv run python example/utils_examples.py
uv run python example/advanced_usage.py
```

To run all examples at once:

```bash
uv run python run_examples.py
```

Each example is self-contained and demonstrates different aspects of the library.