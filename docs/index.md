# MyProject Documentation

## Overview

This is a template Python project that demonstrates best practices for project structure and packaging.

## Installation

```bash
pip install myproject
```

## Usage

### As a Module

```python
from myproject.main import hello

message = hello("Python Developer")
print(message)  # Hello, Python Developer!
```

### Command Line

```bash
# Basic usage
python -m myproject.main

# With custom name
python -m myproject.main --name "Developer"

# Using the CLI entry point (if installed)
myproject --name "Developer"
```

## API Reference

### `hello(name="World")`

Generate a greeting message.

**Parameters:**
- `name` (str): The name to greet (default: "World")

**Returns:**
- `str`: A greeting message

**Example:**
```python
message = hello("Alice")
# Returns: "Hello, Alice!"
```