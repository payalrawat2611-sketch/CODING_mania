What is Polymorphism?

Polymorphism means “many forms.” In OOP, the same method or operation can behave differently depending on the object.

1. Method Overriding

A child class can provide its own version of a method defined in the parent class.

class Animal:
    def sound(self):
        print("Animal makes a sound")

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

Output:

Dog barks
Cat meows
2. Polymorphism with Functions
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

def make_sound(animal):
    animal.sound()

make_sound(Dog())
make_sound(Cat())

The same make_sound() function works with different objects.

Remember
Inheritance → acquiring properties/methods from another class.
Polymorphism → same method/interface, different behavior.
Method overriding is the most common example of polymorphism in Python