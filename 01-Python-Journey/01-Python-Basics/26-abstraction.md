What is Abstraction?

Abstraction means hiding unnecessary implementation details and showing only the essential features to the user.

Real-life example

When you use an ATM, you simply:

Insert your card
Enter PIN
Select amount
Get cash

You don't need to know how the ATM internally communicates with the bank.

That's abstraction — you use the functionality without worrying about its internal implementation.

Abstraction in Python

Python provides abstraction using the abc module.

ABC → Abstract Base Class
@abstractmethod → Defines a method that must be implemented by child classes.
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Dog barks")


class Cat(Animal):

    def sound(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
Output
Dog barks
Cat meows
Why use @abstractmethod?

It forces child classes to provide their own implementation.

For example:

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

Here, Animal says:

"Every animal must have a sound() method, but I won't decide what that sound is."

Then:

class Dog(Animal):
    def sound(self):
        print("Bark")

Dog decides how sound() works.

Abstract Class Cannot Be Directly Instantiated
animal = Animal()

This gives an error because Animal contains an abstract method that hasn't been implemented.

But this works:

dog = Dog()

because Dog provides the required sound() implementation.

Abstraction vs Encapsulation

These are easy to confuse:

## Concept	Meaning
Abstraction	Hides implementation details
Encapsulation	Hides/protects data and internal state

Easy way to remember:

Abstraction = What to show
Encapsulation = What to protect

## Key points for revision
Use the abc module for formal abstraction.
ABC is used to create an abstract base class.
@abstractmethod defines a method that child classes must implement.
Abstract classes generally act as a blueprint.
You cannot instantiate a class while it still has unimplemented abstract methods.
Abstraction makes code easier to design, maintain, and extend.