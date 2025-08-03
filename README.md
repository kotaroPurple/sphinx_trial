# sphinx-trial

A sample Python library demonstrating multiple modules with Sphinx documentation.

## Installation

```bash
uv venv
uv pip install -e .
```

## Quick Start

```python
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
```

## Examples

See the `example/` directory for comprehensive usage examples:

```bash
uv run python run_examples.py
```

## Modules

- **math**: Calculator and geometry classes
- **text**: Text formatting and validation utilities
- **utils**: Logging and configuration management

## Documentation

Comprehensive documentation is available:

- **Installation Guide**: Step-by-step setup instructions
- **Tutorial**: Learn the basics with guided examples
- **API Reference**: Complete function and class documentation
- **Examples**: Real-world usage patterns

Build documentation locally:

```bash
# Using taskipy (recommended)
uv run task docs

# Or using script directly
uv run python build_docs.py

# Open docs/_build/html/index.html in your browser
```

## Development

For development setup and contribution guidelines, see [DEVELOPMENT.md](DEVELOPMENT.md).

Quick development setup:

```bash
# Setup environment
python dev_setup.py
# or
make setup
# or
uv run task setup

# Common development tasks
uv run task examples    # Run all examples
uv run task docs       # Build documentation
uv run task docs-serve # Build and serve docs locally
uv run task docs-clean # Clean documentation build
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.