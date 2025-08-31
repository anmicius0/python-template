"""
Main module for MyProject.

This module contains the core functionality of the project.
"""

import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def hello(name: str = "World") -> str:
    """
    Generate a greeting message.
    
    Args:
        name: The name to greet (default: "World")
        
    Returns:
        A greeting message
    """
    message = f"Hello, {name}!"
    logger.info(message)
    return message


def main() -> None:
    """
    Main function that serves as the entry point when running the module directly.
    """
    print(hello())


if __name__ == "__main__":
    main()