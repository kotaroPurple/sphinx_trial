"""Text formatting utilities."""

import re


class TextFormatter:
    """Text formatting and manipulation utilities."""

    def capitalize_words(self, text: str) -> str:
        """Capitalize the first letter of each word.
        
        Args:
            text: Input text
            
        Returns:
            Text with capitalized words
        """
        return text.title()

    def remove_spaces(self, text: str) -> str:
        """Remove all whitespace from text.
        
        Args:
            text: Input text
            
        Returns:
            Text with all spaces removed
        """
        return re.sub(r'\s+', '', text)

    def truncate(self, text: str, max_length: int, suffix: str = "...") -> str:
        """Truncate text to specified length.
        
        Args:
            text: Input text
            max_length: Maximum length of output
            suffix: Suffix to add when truncating
            
        Returns:
            Truncated text with suffix if needed
        """
        if len(text) <= max_length:
            return text
        return text[:max_length - len(suffix)] + suffix