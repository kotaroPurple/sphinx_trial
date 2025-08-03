"""Utils module usage examples."""

from sphinx_trial.utils import SimpleLogger, Config

def logger_examples():
    """Demonstrate SimpleLogger usage."""
    print("=== Logger Examples ===")
    
    # Default logger
    logger = SimpleLogger()
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    
    # Named logger
    app_logger = SimpleLogger("MyApp")
    app_logger.info("Application started")
    app_logger.warning("Low memory warning")

def config_examples():
    """Demonstrate Config usage."""
    print("\n=== Config Examples ===")
    
    config = Config()
    
    # Set configuration values
    config.set("app_name", "sphinx-trial")
    config.set("version", "1.0.0")
    config.set("debug", True)
    config.set("max_connections", 100)
    
    # Get configuration values
    print(f"App name: {config.get('app_name')}")
    print(f"Version: {config.get('version')}")
    print(f"Debug mode: {config.get('debug')}")
    print(f"Max connections: {config.get('max_connections')}")
    
    # Get with default value
    print(f"Timeout (default): {config.get('timeout', 30)}")
    
    # Check if key exists
    print(f"Has 'app_name': {config.has('app_name')}")
    print(f"Has 'missing_key': {config.has('missing_key')}")
    
    # Get all config as dict
    print(f"All config: {config.to_dict()}")

def main():
    """Run all utils examples."""
    logger_examples()
    config_examples()

if __name__ == "__main__":
    main()