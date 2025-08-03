# Makefile for sphinx-trial development

.PHONY: help setup install examples docs docs-clean test clean all

help:  ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

setup:  ## Set up development environment
	@python dev_setup.py

install:  ## Install package in editable mode
	@uv pip install -e .

install-docs:  ## Install package with documentation dependencies
	@uv pip install -e ".[docs]"

examples:  ## Run all examples
	@uv run python run_examples.py

docs:  ## Build documentation
	@uv run python build_docs.py

docs-clean:  ## Clean documentation build directory
	@uv run python build_docs.py clean

docs-serve:  ## Build docs and serve locally (requires python -m http.server)
	@uv run python build_docs.py
	@echo "Starting local server at http://localhost:8000"
	@cd docs/_build/html && python -m http.server 8000

test:  ## Run tests (placeholder for future tests)
	@echo "Tests not implemented yet"

clean:  ## Clean build artifacts
	@rm -rf build/
	@rm -rf dist/
	@rm -rf *.egg-info/
	@rm -rf docs/_build/
	@find . -type d -name __pycache__ -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete

all: setup examples docs  ## Set up environment, run examples, and build docs