"""Simple logging utility."""

from datetime import datetime
from typing import Optional


class SimpleLogger:
    """A simple logger for basic logging needs."""

    def __init__(self, name: str = "sphinx_trial") -> None:
        """Initialize logger with a name.
        
        Args:
            name: Logger name
        """
        self.name = name

    def _format_message(self, level: str, message: str) -> str:
        """Format log message with timestamp and level.
        
        Args:
            level: Log level
            message: Log message
            
        Returns:
            Formatted log message
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"[{timestamp}] {level} - {self.name}: {message}"

    def info(self, message: str) -> None:
        """Log info message.
        
        Args:
            message: Message to log
        """
        print(self._format_message("INFO", message))

    def warning(self, message: str) -> None:
        """Log warning message.
        
        Args:
            message: Message to log
        """
        print(self._format_message("WARNING", message))

    def error(self, message: str) -> None:
        """Log error message.
        
        Args:
            message: Message to log
        """
        print(self._format_message("ERROR", message))