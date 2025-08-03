"""sphinx-trial: A sample Python library with multiple modules."""

from . import math, text, utils
from .math import Calculator, Circle, Rectangle
from .text import TextFormatter, is_email, is_phone, is_url
from .utils import SimpleLogger, Config

__version__ = "0.1.0"
__all__ = [
    "math", "text", "utils",
    "Calculator", "Circle", "Rectangle",
    "TextFormatter", "is_email", "is_phone", "is_url",
    "SimpleLogger", "Config"
]

def hello() -> str:
    """Return a greeting message.
    
    Returns:
        Greeting message
    """
    return "Hello from sphinx-trial!"
