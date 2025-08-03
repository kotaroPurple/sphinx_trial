"""Text module usage examples."""

from sphinx_trial.text import TextFormatter, is_email, is_phone, is_url

def formatter_examples():
    """Demonstrate TextFormatter usage."""
    print("=== Text Formatter Examples ===")
    formatter = TextFormatter()
    
    # Capitalize words
    text = "hello world python"
    print(f"Original: '{text}'")
    print(f"Capitalized: '{formatter.capitalize_words(text)}'")
    
    # Remove spaces
    spaced_text = "remove all spaces"
    print(f"With spaces: '{spaced_text}'")
    print(f"No spaces: '{formatter.remove_spaces(spaced_text)}'")
    
    # Truncate text
    long_text = "This is a very long text that needs to be truncated"
    print(f"Long text: '{long_text}'")
    print(f"Truncated (20): '{formatter.truncate(long_text, 20)}'")
    print(f"Truncated (30, custom): '{formatter.truncate(long_text, 30, '...')}'")

def validation_examples():
    """Demonstrate validation functions."""
    print("\n=== Validation Examples ===")
    
    # Email validation
    emails = ["user@example.com", "invalid-email", "test@domain.co.jp"]
    print("Email validation:")
    for email in emails:
        print(f"  '{email}': {is_email(email)}")
    
    # Phone validation
    phones = ["123-456-7890", "1234567890", "invalid", "+1-555-123-4567"]
    print("Phone validation:")
    for phone in phones:
        print(f"  '{phone}': {is_phone(phone)}")
    
    # URL validation
    urls = ["https://example.com", "http://test.org/path", "invalid-url", "https://domain.co.jp"]
    print("URL validation:")
    for url in urls:
        print(f"  '{url}': {is_url(url)}")

def main():
    """Run all text examples."""
    formatter_examples()
    validation_examples()

if __name__ == "__main__":
    main()