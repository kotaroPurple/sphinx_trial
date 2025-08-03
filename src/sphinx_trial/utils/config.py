"""Configuration management utility."""

from typing import Any, Dict, Optional


class Config:
    """Simple configuration manager."""

    def __init__(self) -> None:
        """Initialize empty configuration."""
        self._data: Dict[str, Any] = {}

    def set(self, key: str, value: Any) -> None:
        """Set configuration value.
        
        Args:
            key: Configuration key
            value: Configuration value
        """
        self._data[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value.
        
        Args:
            key: Configuration key
            default: Default value if key not found
            
        Returns:
            Configuration value or default
        """
        return self._data.get(key, default)

    def has(self, key: str) -> bool:
        """Check if configuration key exists.
        
        Args:
            key: Configuration key
            
        Returns:
            True if key exists, False otherwise
        """
        return key in self._data

    def clear(self) -> None:
        """Clear all configuration data."""
        self._data.clear()

    def to_dict(self) -> Dict[str, Any]:
        """Get all configuration as dictionary.
        
        Returns:
            Copy of configuration data
        """
        return self._data.copy()