# ⚠️ Python Exception Handling


## What is an Exception?


An exception is an error that occurs while a program is running.


Example:


```python
a = 10
b = 0


print(a / b)

This gives a ZeroDivisionError.

try and except

try contains code that may cause an error, while except handles the error.

try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
Handling Multiple Exceptions
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
else

else runs when no exception occurs.

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
else:
    print("You entered:", num)
finally

finally always executes, whether an exception occurs or not.

try:
    print(10 / 2)
except ZeroDivisionError:
    print("Error")
finally:
    print("Program completed")
raise

raise is used to manually generate an exception.

age = -1


if age < 0:
    raise ValueError("Age cannot be negative")
Remember
try → Code that may cause an error
except → Handles the error
else → Runs when there is no error
finally → Always runs
raise → Manually raises an exception