What is a Decorator?

A decorator is a function that adds extra functionality to another function without changing its original code.

Basic Example
def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper


@decorator
def greet():
    print("Hello!")


greet()

Output:

Before function
Hello!
After function
@ Syntax
@decorator
def greet():
    print("Hello!")

is equivalent to:

def greet():
    print("Hello!")


greet = decorator(greet)
Decorator with Arguments

When the original function takes arguments, use *args and **kwargs.

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Function is running")
        return func(*args, **kwargs)
    return wrapper


@decorator
def add(a, b):
    return a + b


print(add(10, 20))
Why Use Decorators?

Decorators are commonly used for:

Logging
Authentication
Checking permissions
Measuring execution time
Validation
Adding reusable functionality
🧠 Remember
Decorator → modifies a function's behavior.
@decorator → applies a decorator.
wrapper() → usually contains the additional functionality.
*args, **kwargs → allows handling different arguments.
Decorators are based on functions being treated as objects.