# Calculator

A simple command-line calculator written in Python that supports basic arithmetic operations with input validation and continuous calculation mode.

## Features

- **Six Operations**: Addition, subtraction, multiplication, division, modulo, and exponentiation
- **Input Validation**: Validates both operator and numeric inputs
- **Division Safety**: Handles division by zero gracefully
- **Continuous Mode**: Perform multiple calculations without restarting
- **Float Support**: Works with decimal numbers

## Supported Operations

| Operator | Operation | Example |
|----------|-----------|---------|
| `+` | Addition | `5 + 3 = 8` |
| `-` | Subtraction | `10 - 4 = 6` |
| `*` | Multiplication | `6 * 7 = 42` |
| `/` | Division | `15 / 3 = 5` |
| `%` | Modulo (remainder) | `17 % 5 = 2` |
| `^` | Exponentiation (power) | `2 ^ 8 = 256` |

## Installation

```bash
git clone https://github.com/KasGreen/calculator.git
cd calculator
```

## Usage

Run the calculator:

```bash
python calculator.py
```

### Interactive Session Example

```
Would you like to +, -, *, /, % or ^: +
Please enter your first number: 10
Please enter your second number: 5
15.0
Would you like to perform another calculation y/n: y

Would you like to +, -, *, /, % or ^: ^
Please enter your first number: 2
Please enter your second number: 10
1024.0
Would you like to perform another calculation y/n: n
```

## API Reference

The calculator provides modular functions that can be imported and used separately:

```python
from calculator import add_numbers, subtract_numbers, multiply_numbers, divide_numbers, mod_numbers, power_of_numbers
```

### Functions

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `add_numbers(num1, num2)` | Two numbers | float | Returns the sum of two numbers |
| `subtract_numbers(num1, num2)` | Two numbers | float | Returns the difference (num1 - num2) |
| `multiply_numbers(num1, num2)` | Two numbers | float | Returns the product of two numbers |
| `divide_numbers(num1, num2)` | Two numbers | float or None | Returns the quotient; prints error and returns None if num2 is 0 |
| `mod_numbers(num1, num2)` | Two numbers | float | Returns the remainder of num1 divided by num2 |
| `power_of_numbers(num1, num2)` | Two numbers | float | Returns num1 raised to the power of num2 |

### Programmatic Usage

```python
from calculator import add_numbers, divide_numbers, power_of_numbers

# Basic operations
result = add_numbers(10, 5)        # 15
result = divide_numbers(20, 4)     # 5.0
result = power_of_numbers(2, 8)    # 256

# Division by zero protection
result = divide_numbers(10, 0)     # Prints "Cannot divide by 0", returns None
```

## Input Validation

The calculator validates all inputs:

### Operator Validation
- Only accepts: `+`, `-`, `*`, `/`, `%`, `^`
- Empty input prompts re-entry
- Invalid operators prompt re-entry

### Number Validation
- Accepts integers and floating-point numbers
- Non-numeric input prompts re-entry
- Uses Python's `float()` for parsing

## Error Handling

| Scenario | Behavior |
|----------|----------|
| Division by zero | Prints "Cannot divide by 0" and returns `None` |
| Invalid operator | Prints "Please enter a valid operator" and re-prompts |
| Non-numeric input | Prints "Please enter a number" and re-prompts |
| Empty operator | Prints "Please enter an operator" and re-prompts |

## Examples

### Basic Arithmetic
```python
add_numbers(100, 50)        # 150
subtract_numbers(100, 50)   # 50
multiply_numbers(12, 12)    # 144
divide_numbers(100, 4)      # 25.0
```

### Modulo Operations
```python
mod_numbers(17, 5)    # 2 (17 = 5*3 + 2)
mod_numbers(100, 7)   # 2 (100 = 7*14 + 2)
mod_numbers(25, 5)    # 0 (evenly divisible)
```

### Exponentiation
```python
power_of_numbers(2, 10)    # 1024
power_of_numbers(5, 3)     # 125
power_of_numbers(10, 0)    # 1 (any number to power 0)
power_of_numbers(2, -1)    # 0.5 (negative exponents supported)
```

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Author

KasGreen

---

*Note: This is an educational project demonstrating basic Python concepts including functions, input validation, loops, and error handling.*
