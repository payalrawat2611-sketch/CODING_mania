1. What are Magic Methods?

Magic methods are special methods in Python that have double underscores (__) before and after their names.

They allow objects to work with Python's built-in operations.

Examples:

__init__
__str__
__len__
__add__
__eq__
2. __str__()

__str__() defines what should be displayed when an object is printed.

Without __str__():

class Student:
    def __init__(self, name):
        self.name = name

student = Student("Payal")

print(student)

Python displays a default object representation.

With __str__():

class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student: {self.name}"


student = Student("Payal")

print(student)

Output:

Student: Payal
3. __len__()

__len__() allows us to use the len() function with our objects.

class Team:
    def __init__(self, players):
        self.players = players

    def __len__(self):
        return len(self.players)


team = Team(["A", "B", "C", "D"])

print(len(team))

Output:

4
4. __add__()

__add__() defines what happens when we use + between objects.

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


a = Number(10)
b = Number(20)

print(a + b)

Output:

30

Python internally calls:

a.__add__(b)
5. Common Magic Methods
Magic Method	Purpose
__init__()	Initializes object
__str__()	String representation
__len__()	Used by len()
__add__()	+ operation
__sub__()	- operation
__mul__()	* operation
__eq__()	== comparison
__lt__()	< comparison
__gt__()	> comparison
Remember

Magic methods allow your objects to behave like Python's built-in types.

Chapter 30 — Properties in Python

A property allows us to access a method like an attribute while still controlling how the value is accessed or modified.

Python uses the @property decorator.

Example
class Student:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks


student = Student(85)

print(student.marks)

Output:

85

Notice that we use:

student.marks

instead of:

student.marks()

because @property makes the method behave like an attribute.

Setter with Property

We can also control how a value is changed.

class Student:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self._marks = value
        else:
            print("Invalid marks")


student = Student(85)

student.marks = 90

print(student.marks)

Output:

90

If we do:

student.marks = 150

Output:

Invalid marks
Why use Properties?

Properties are useful when you want:

Controlled access to attributes
Validation
Read-only attributes
Cleaner code
Encapsulation
🧠 Quick Revision
Magic Methods
__init__() → initialize
__str__()  → print object
__len__()  → len(object)
__add__()  → object + object
__eq__()   → object == object
Properties
@property
    ↓
Access method like an attribute

@attribute.setter
    ↓
Control how attribute is changed