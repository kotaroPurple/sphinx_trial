# Development Guide

This guide explains how to set up and work with the sphinx-trial project.

## Quick Setup

```bash
# Clone the repository
git clone <repository-url>
cd sphinx-trial

# Set up development environment
python dev_setup.py
# or
make setup
```

## Development Environment

### Requirements
- Python 3.13+
- uv package manager

### Manual Setup
```bash
# Create virtual environment
uv venv

# Install in editable mode with docs dependencies
uv pip install -e ".[docs]"
```

## Common Tasks

### Running Examples
```bash
# Run all examples (taskipy - recommended)
uv run task examples

# Alternative methods
uv run python run_examples.py
make examples

# Run individual examples
uv run python example/basic_usage.py
uv run python example/math_examples.py
uv run python example/text_examples.py
uv run python example/utils_examples.py
uv run python example/advanced_usage.py
```

### Available Taskipy Commands
```bash
uv run task docs        # Build documentation
uv run task docs-clean  # Clean documentation build
uv run task docs-serve  # Build and serve docs at http://localhost:8000
uv run task examples    # Run all examples
uv run task setup       # Set up development environment
uv run task clean       # Clean all build artifacts
```

### Building Documentation
```bash
# Build documentation (taskipy - recommended)
uv run task docs

# Clean and rebuild
uv run task docs-clean

# Build and serve locally
uv run task docs-serve  # Opens http://localhost:8000

# Alternative methods
uv run python build_docs.py
make docs
```

### Development Workflow
```bash
# Make changes to code
# Update docstrings and documentation
# Test changes
uv run task examples

# Build documentation
uv run task docs

# Commit changes
git add .
git commit -m "Description of changes"
```

## Project Structure

```
sphinx-trial/
├── src/sphinx_trial/          # Main library code
│   ├── __init__.py
│   ├── math/                  # Math module
│   ├── text/                  # Text module
│   └── utils/                 # Utils module
├── example/                   # Usage examples
├── docs/                      # Sphinx documentation
│   ├── source files (.rst)
│   └── _build/html/          # Built documentation
├── dev_setup.py              # Development setup script
├── run_examples.py           # Example runner
├── build_docs.py             # Documentation builder
├── Makefile                  # Development commands
└── pyproject.toml            # Project configuration
```

## Code Style

### Docstring Format
Use Google-style docstrings:

```python
def example_function(param1: str, param2: int = 10) -> bool:
    """Brief description of the function.
    
    Longer description if needed.
    
    Args:
        param1: Description of param1
        param2: Description of param2 with default value
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: When param1 is invalid
    """
    pass
```

### Type Hints
- Use type hints for all function parameters and return values
- Import types from `typing` module when needed
- Use `Union[int, float]` for numeric types that accept both

### Error Handling
- Raise appropriate exceptions with descriptive messages
- Document exceptions in docstrings
- Handle edge cases gracefully

## Adding New Features

### Adding a New Module
1. Create directory in `src/sphinx_trial/`
2. Add `__init__.py` with exports
3. Implement classes/functions with docstrings
4. Update main `__init__.py` to export new module
5. Create example in `example/` directory
6. Add API documentation in `docs/api/`
7. Update main documentation if needed

### Adding Examples
1. Create new file in `example/` directory
2. Follow existing example patterns
3. Include comprehensive docstrings
4. Test that example runs correctly
5. Update `example/README.md` if needed

### Updating Documentation
1. Modify relevant `.rst` files in `docs/`
2. Update docstrings in code
3. Build documentation to test changes
4. Check that all links work correctly

## Testing

Currently, the project doesn't have automated tests, but you can verify functionality by:

```bash
# Run all examples
make examples

# Build documentation
make docs

# Manual testing of individual components
uv run python -c "from sphinx_trial import Calculator; print(Calculator().add(1, 2))"
```

## Troubleshooting

### Common Issues

1. **Import errors**: Make sure package is installed in editable mode
   ```bash
   uv pip install -e .
   ```

2. **Documentation build fails**: Check that all dependencies are installed
   ```bash
   uv pip install -e ".[docs]"
   ```

3. **Examples don't run**: Verify virtual environment is activated and package is installed

### Getting Help

- Check existing documentation in `docs/`
- Review example code in `example/`
- Look at similar implementations in the codebase
- Check git history for context on changes

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes following the code style
4. Add examples and documentation
5. Test your changes
6. Submit a pull request

## Release Process

1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md` (when created)
3. Build and test documentation
4. Create git tag
5. Build and publish package (when ready)