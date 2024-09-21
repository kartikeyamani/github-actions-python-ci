def add(a, b):
    """This function returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """This function returns the difference between two numbers."""
    return a - b

def divide(a, b):
    """This function returns the division of two numbers.
    It handles division by zero by returning None."""
    if b == 0:
        print(" Division Error: Division by zero is not allowed.")
        return None
    return a / b
