# 📦 Python Modules & Packages


## What is a Module?


A module is a Python file (`.py`) containing functions, variables, or classes that can be reused in another program.


## Importing a Module


```python
import math


print(math.sqrt(25))
print(math.pi)
Importing Specific Functions
from math import sqrt


print(sqrt(36))
Using an Alias
import math as m


print(m.sqrt(49))
Useful Built-in Modules
math
import math


print(math.sqrt(16))
print(math.factorial(5))
print(math.pi)
random
import random


print(random.randint(1, 10))
datetime
import datetime


print(datetime.datetime.now())
What is a Package?

A package is a collection of related Python modules organized inside a directory.

Example:

my_package/
    __init__.py
    calculator.py
    operations.py
Module vs Package
Module → A single .py file.
Package → A folder containing multiple Python modules.
Remember
import is used to use a module.
from ... import ... imports specific items.
as creates an alias.
Python provides many built-in modules.
Packages help organize large Python projects.