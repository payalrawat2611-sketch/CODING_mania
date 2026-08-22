Python provides different types of methods depending on whether they work with an object, the class, or neither.

1. Instance Method

An instance method works with the object and uses self.

class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)


student = Student("Payal")
student.display()

Here, self refers to the current object.

2. Class Method

A class method works with the class itself rather than a particular object.

It uses the @classmethod decorator and cls.

class Student:
    college = "SGSITS"

    @classmethod
    def change_college(cls, new_college):
        cls.college = new_college


print(Student.college)

Student.change_college("IIT Indore")

print(Student.college)

Output:

SGSITS
IIT Indore

Here, cls refers to the class.

When to use it?

Use a class method when you need to access or modify class-level data.

3. Static Method

A static method doesn't need self or cls.

It uses the @staticmethod decorator.

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b


print(Calculator.add(10, 20))

Output:

30

The method is inside the class because it is logically related to the class, but it doesn't need any object or class data.

Difference Between the Three
Method	First parameter	Works with
Instance method	self	Object
Class method	cls	Class
Static method	None	Independent operation
Easy way to remember
self → Object
cls  → Class
none → Static
🧠 Remember
Instance method → uses self
Class method → uses @classmethod and cls
Static method → uses @staticmethod
Class methods can modify class variables.
Static methods don't automatically receive object or class information.
Quick Example
class Student:
    college = "SGSITS"

    def __init__(self, name):
        self.name = name

    def show_name(self):             # Instance method
        print(self.name)

    @classmethod
    def show_college(cls):           # Class method
        print(cls.college)

    @staticmethod
    def add(a, b):                   # Static method
        return a + b