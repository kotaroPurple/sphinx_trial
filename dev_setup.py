#!/usr/bin/env python3
"""Development environment setup script."""

import subprocess
import sys
from pathlib import Path

def run_command(cmd, description):
    """Run a command and handle errors."""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        if e.stdout:
            print(f"stdout: {e.stdout}")
        if e.stderr:
            print(f"stderr: {e.stderr}")
        return False

def setup_environment():
    """Set up development environment."""
    print("🚀 Setting up sphinx-trial development environment")
    print("=" * 50)
    
    # Check if uv is available
    if not run_command("uv --version", "Checking uv installation"):
        print("❌ uv is not installed. Please install uv first.")
        return False
    
    # Create virtual environment if it doesn't exist
    venv_path = Path(".venv")
    if not venv_path.exists():
        if not run_command("uv venv", "Creating virtual environment"):
            return False
    else:
        print("✅ Virtual environment already exists")
    
    # Install package in editable mode with docs dependencies
    if not run_command("uv pip install -e '.[docs]'", "Installing package with dependencies"):
        return False
    
    # Test installation
    if not run_command("uv run python -c 'from sphinx_trial import hello; print(hello())'", "Testing installation"):
        return False
    
    print("\n" + "=" * 50)
    print("🎉 Development environment setup complete!")
    print("\n📋 Next steps:")
    print("  • Run examples: uv run python run_examples.py")
    print("  • Build docs: uv run python build_docs.py")
    print("  • Run tests: uv run python -m pytest (when tests are added)")
    
    return True

if __name__ == "__main__":
    success = setup_environment()
    sys.exit(0 if success else 1)