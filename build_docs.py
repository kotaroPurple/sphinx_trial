#!/usr/bin/env python3
"""Script to build Sphinx documentation."""

import subprocess
import sys
from pathlib import Path

def build_docs():
    """Build Sphinx documentation."""
    docs_dir = Path("docs")
    build_dir = docs_dir / "_build" / "html"
    
    print("Building Sphinx documentation...")
    print(f"Source: {docs_dir}")
    print(f"Output: {build_dir}")
    print("-" * 50)
    
    try:
        # Build HTML documentation
        result = subprocess.run([
            sys.executable, "-m", "sphinx",
            "-b", "html",
            str(docs_dir),
            str(build_dir)
        ], check=True)
        
        print("-" * 50)
        print("✅ Documentation built successfully!")
        print(f"📁 Open: {build_dir / 'index.html'}")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error building documentation: {e}")
        return False

def clean_docs():
    """Clean documentation build directory."""
    build_dir = Path("docs") / "_build"
    
    if build_dir.exists():
        import shutil
        shutil.rmtree(build_dir)
        print("🧹 Cleaned documentation build directory")
    else:
        print("📁 Build directory doesn't exist")

def main():
    """Main function."""
    if len(sys.argv) > 1 and sys.argv[1] == "clean":
        clean_docs()
    else:
        build_docs()

if __name__ == "__main__":
    main()