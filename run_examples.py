#!/usr/bin/env python3
"""Script to run all examples."""

import subprocess
import sys
from pathlib import Path

def run_example(example_file):
    """Run a single example file."""
    print(f"\n{'='*50}")
    print(f"Running: {example_file}")
    print('='*50)
    
    try:
        result = subprocess.run([sys.executable, f"example/{example_file}"], 
                              capture_output=False, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running {example_file}: {e}")
        return False

def main():
    """Run all example files."""
    examples = [
        "basic_usage.py",
        "math_examples.py", 
        "text_examples.py",
        "utils_examples.py",
        "advanced_usage.py"
    ]
    
    print("Running all sphinx-trial examples...")
    
    success_count = 0
    for example in examples:
        if run_example(example):
            success_count += 1
    
    print(f"\n{'='*50}")
    print(f"Completed: {success_count}/{len(examples)} examples ran successfully")
    print('='*50)

if __name__ == "__main__":
    main()