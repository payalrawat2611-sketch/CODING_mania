What is Encapsulation?

Encapsulation means bundling data and methods together inside a class and controlling access to the data.

Think of it as:

Keeping data protected and allowing controlled access to it.

Example
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")


s1 = Student("Payal", 85)

print(s1.name)
print(s1.get_marks())

s1.set_marks(90)

print(s1.get_marks())

Here:

self.__marks

uses __, making it a private attribute.

You shouldn't directly access it like:

print(s1.__marks)

Instead, we use methods such as:

get_marks()
set_marks()

This allows us to control how the data is accessed or changed.

Access Modifiers in Python

Python doesn't have strict private, protected, and public keywords like Java. Instead, naming conventions are used:

Syntax	Meaning
name	Public
_name	Protected convention
__name	Private/name mangling
Easy Example to Remember
Class
 ├── Data
 └── Methods
       ↓
   Controlled Access
Abstraction vs Encapsulation

Abstraction: Hide unnecessary implementation details.

Encapsulation: Protect data and control access to it.

Important for DSA/Interviews

Remember these four major OOP concepts:

Encapsulation → Data protection
Abstraction → Hide implementation
Inheritance → Reuse existing code
Polymorphism → One interface, different behavior